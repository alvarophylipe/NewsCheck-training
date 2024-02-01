function submitForm () {
    var type = document.getElementById("type").value;
    var text = document.getElementById("text").value;

    fetch('/detector/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'type=' + encodeURIComponent(type) + '&text=' + encodeURIComponent(text),
    })
    .then(response => response.json())
    .then(data => {
        exibirResultado(data.prediction)
    })
}

function exibirResultado(resultado) {
    var resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '<p> Resultado: ' + resultado + '</p>';
}