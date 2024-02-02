function changePlaceholder() {
    var selectedValue = document.getElementById("type").value;

    var input = document.getElementById("text");

    if (selectedValue === "link") {
        input.placeholder = "Cole o link aqui...";
    } else {
        input.placeholder = "Cole o texto aqui..."
    }

}

class FormValidation {
    constructor() {
        this.form = document.querySelector('.forms');
        this.button = document.getElementById('loadingButton')
        this.spinner = document.createElement('div');
        this.spinner.classList.add('loading-spinner', 'text-center');
        this.events();
    }

    events() {
        this.form.addEventListener('submit', e => {
            this.handleSubmit(e);
        });

    }

    handleSubmit(e) {
        e.preventDefault();
        const typeInput = document.getElementById("type").value;
        const textInput = document.getElementById("text");
        
        console.log(this.button)
        this.showLoadingSpinner();

        if (typeInput === 'link') {
            this.submitLinkType(typeInput, textInput)
        }

        this.submitTextType(typeInput, textInput);


    }

    showLoadingSpinner() {
        this.button.addEventListener("click"), () => {
            this.button.classList.remove('btn')
        }
    }

    hideLoadingSpinner() {
        this.button.innerHTML = ''
        this.button.disabled = false;
    }

    submitTextType(typeInput, textInput){
        this.cleanErrorText();

        const text = textInput.value;

        const words = this.countWords(text);

        if (words < 30) {
            this.createError(textInput, 'Texto muito pequeno.');
            return;
        }

        this.submitForm(typeInput, text);

    }

    submitLinkType(typeInput, textInput) {
        this.cleanErrorText()

        const text = textInput.value

        if (!this.isLink(text)) {
            this.createError(textInput, 'Insira um link válido.');
            return;
        }
        
        this.submitForm(typeInput, text)

    }

    isLink(text) {
        const regex = /^(ftp|http|https):\/\/[^ "]+$/;
        return regex.test(text);
    }

    countWords(text) {
        return text.trim().split(/\s+/).length;
    } 

    createError(field, msg) {
        const div = document.createElement('div');
        div.innerHTML = msg;
        div.classList.add('error-text', 'text-danger', 'text-center', 'mt-2');
        field.insertAdjacentElement('afterend', div);
    }

    

    submitForm(type, text) {
        fetch('/detector/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'type=' + encodeURIComponent(type) + '&text=' + encodeURIComponent(text),
        })
        .then(response => response.json())
        .then(data => {
            this.showResult(data.prediction)
        })
    }
    
    showResult(resultado) {
        var resultDiv = document.getElementById('result');
        resultDiv.innerHTML = '<p> Resultado: ' + resultado + '</p>';
    }

    cleanErrorText() {
        const errorText = this.form.querySelector('.error-text')
        if (errorText) {
            errorText.remove()
        }
    }
}

const validate = new FormValidation