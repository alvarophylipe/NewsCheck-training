// Static class for user interface interactions
class UIHandler {
    static input = document.getElementById("text");
    static backgroundAnimation = document.getElementById("backgroundAnimation");
    static output = document.getElementById("outputText");

    // Change the placeholder of the text input base on the selected type
    static changePlaceholder(type) {
        this.input.placeholder = type === "link" ? "Cole o link aqui..." : "Cole o texto aqui..."; 
    }

    // Display the result on the user interface
    static showResult(result) {
        
        const trueLabelText = "Me parece verdadeira! 👍 É sempre bom verificar antes de divulgar, que tal buscar outras fontes?";
        const fakeLabelText = "Hmm... Pode ser falsa! 👎 Verifique com fontes confiáveis!";

        this.output.innerHTML = result === 1 ? fakeLabelText : trueLabelText;

        UIHandler.addBackgroundAnimation(result);
    }

    // Show the loading spinner 
    static showSpinner() {
        document.getElementById('spinner').classList.remove('hidden');
        document.getElementById('sendImg').classList.add('hidden');
    } 
    
    // Hide the loading spinner 
    static hideSpinner(){
        document.getElementById('sendImg').classList.remove('hidden');
        document.getElementById('spinner').classList.add('hidden');
    }

    // Create an error message
    static createError(field, msg) {
        var div = document.createElement('div');
        div.classList.add('error-text', 'text-danger', 'text-center', 'mt-2');
        div.innerHTML = msg;
        field.insertAdjacentElement('afterend', div);
    }

    // Remove existing error messages
    static removeErrorText() {
        const errorTextDiv = document.querySelector('.error-text');
        if (errorTextDiv) {
            errorTextDiv.remove();
        }
    }

    // Add background animation based on the result
    static addBackgroundAnimation(result) {
        this.backgroundAnimation.classList.add(result === 1 ? "circle-fake" : "circle-true");
    }

    // Remove the background animation
    static removeBackgroundAnimation() {
        this.backgroundAnimation.classList.remove("circle-fake", "circle-true");
    }

    // Show request error
    static showRequestError() {
        const reqErrorText = "Parece que estou com um problema. 🛠️ Tente novamente mais tarde!";
        this.output.innerHTML = reqErrorText;
    }

}

// Class responsible for form validation and handling
class FormValidation {
    constructor() {
        // Get references to elements and initialize events
        this.form = document.querySelector('.forms');
        this.events();
    }

    // Add events to the form
    events() {
        this.form.addEventListener('submit', e => this.handleSubmit(e)); 
    }

    // Handle form submission
    handleSubmit(e) {
        e.preventDefault();
        const typeInput = document.getElementById("type").value;
        
        // try{
            // Determine validation type
            if (typeInput === 'link') {
                this.submitLinkType();
            } else {
                this.submitTextType();
            }
        // } catch {
        //     UIHandler.showRequestError();
        //     UIHandler.hideSpinner();
        // }
    }

    // Handle form submission for text type
    submitTextType(){
        UIHandler.removeErrorText();

        const text = document.getElementById("text").value;
        const words = this.countWords(text);

        if (words < 30) {
            UIHandler.createError(textInput, 'Texto muito pequeno.');
            UIHandler.hideSpinner();
            return;
        }

        UIHandler.showSpinner();
        this.submitForm('text', text);

    }

    // Handle form submission for link type
    submitLinkType() {
        UIHandler.removeErrorText()

        const link = document.getElementById("link").value;

        if (!this.isLink(link)) {
            UIHandler.createError(textInput, 'Insira um link válido.');
            return;
        }
        
        UIHandler.showSpinner();
        this.submitForm('link', link)

    }

    // Check if the text is a valid link
    isLink(text) {
        const regex = /^(ftp|http|https):\/\/[^ "]+$/;
        return regex.test(text);
    }

    // Count words in a text
    countWords(text) {
        return text.trim().split(/\s+/).length;
    } 

    // Submit the form via a fetch request
    submitForm(type, text) {
        UIHandler.showSpinner();
        UIHandler.removeBackgroundAnimation();

        fetch('/check/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'type=' + encodeURIComponent(type) + '&text=' + encodeURIComponent(text),
        })
        .then(response => response.json())
        .then(data => {
            UIHandler.showResult(data.prediction);
            UIHandler.hideSpinner();
        })
        .catch(() => {
            UIHandler.showRequestError();
            UIHandler.hideSpinner();
        })
    }
}

// Execution
const validate = new FormValidation();
document.getElementById("type").addEventListener("change", (event) => UIHandler.changePlaceholder(event.target.value));
