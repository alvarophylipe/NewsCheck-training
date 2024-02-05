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
        this.spinner = document.getElementById('spinner');
        this.sendImg = document.getElementById('sendImg');
        this.circleAnimation = document.getElementById("circleAnimation")
        this.events();
    }

    events() {
        this.form.addEventListener('submit', e => {
            this.handleSubmit(e);
        });
        
        this.hideLoadingSpinner();
    }

    handleSubmit(e) {
        e.preventDefault();
        const typeInput = document.getElementById("type").value;
        const textInput = document.getElementById("text");

        if (typeInput === 'link') {
            this.submitLinkType(typeInput, textInput);
        } else {
            this.submitTextType(typeInput, textInput);
        }

    }

    showLoadingSpinner() {
        this.sendImg.classList.add('hidden');
        this.spinner.classList.remove('hidden');
    }

    hideLoadingSpinner() {
        this.spinner.classList.add('hidden');
        this.sendImg.classList.remove('hidden');
    }

    submitTextType(typeInput, textInput){
        this.cleanErrorText();

        const text = textInput.value;

        const words = this.countWords(text);

        if (words < 30) {
            this.createError(textInput, 'Texto muito pequeno.');
            this.hideLoadingSpinner();
            return;
        }

        this.showLoadingSpinner();
        this.submitForm(typeInput, text);

    }

    submitLinkType(typeInput, textInput) {
        this.cleanErrorText()

        const text = textInput.value

        if (!this.isLink(text)) {
            this.createError(textInput, 'Insira um link válido.');
            return;
        }
        
        this.showLoadingSpinner();
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
    
    backgroundAnimation(result) {
        if (result === 0) {
            this.circleAnimation.classList.add('circle-true');
        } else {
            this.circleAnimation.classList.add('circle-fake');
        }
    }

    clearAnimation() {
        this.circleAnimation.classList.remove('circle-true', 'circle-fake');
    }

    submitForm(type, text) {
        this.showLoadingSpinner();
        this.clearAnimation();
        fetch('/detector/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'type=' + encodeURIComponent(type) + '&text=' + encodeURIComponent(text),
        })
        .then(response => response.json())
        .then(data => {
            this.showResult(data.prediction);
        })
    }
    
    showResult(result) {
        this.hideLoadingSpinner();
        this.backgroundAnimation(result);
        var resultDiv = document.getElementById('result');
        resultDiv.innerHTML = '<p> Resultado: ' + result + '</p>';
    }

    cleanErrorText() {
        const errorText = this.form.querySelector('.error-text');
        if (errorText) {
            errorText.remove();
        }
    }
}

// showSpinner()
const validate = new FormValidation;