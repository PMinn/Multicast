const textValue = document.getElementById('textValue');
const connectingBtn = document.getElementById('connectingBtn');

connectingBtn.addEventListener('click', () => {
    var v = textValue.value.toString()
    eel.send(v);
});