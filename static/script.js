const infoMsg = document.querySelector(".info-msg")
const successMsg = document.querySelector(".success-msg")

const messages = [infoMsg, successMsg]

messages.forEach( msg => {

async function delayMsg() {
    // Função que baixa a opacidade e depois remove a noticação da DOM
    await new Promise(res => setTimeout(res, 4000));
    msg.style.opacity = 0;
    await new Promise(res => setTimeout(res, 1000));
    msg.remove();
    }


    delayMsg()

})



