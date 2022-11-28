// const ip = document.getElementById('ip');
const textValue = document.getElementById('textValue');
const connectingBtn = document.getElementById('connectingBtn');

connectingBtn.addEventListener('click', () => {
    var v = textValue.value.toString()
    eel.send(v);
    writeMsg(0, v)
});