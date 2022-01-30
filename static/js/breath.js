// variables
const circleProgress = document.querySelector('.circle-progress');
const numberOfBreaths = document.querySelector('.breath-input');
const start = document.querySelector('.start');
const instructions = document.querySelector('.instructions');
const breathsText= document.querySelector('.breaths-text');
let breathsLeft = 3;


// watch for selected breath(number) from user and update
numberOfBreaths.addEventListener('change', () => {
    breathsLeft = numberOfBreaths.value;
    breathsText.innerText = breathsLeft;
});


// grow and shrink breath circle
const growCircle = () => {
    circleProgress.classList.add('circle-grow');
    setTimeout(() => {
        circleProgress.classList.remove('circle-grow');
    }, 8000);
};


// breathing instructions
const breathTextUpdate = () => {
    breathsLeft--;
    breathsText.innerText = breathsLeft;
    instructions.innerText = "Breathe in";
    setTimeout(() => {
        instructions.innerText = "Hold Your Breath";
        setTimeout(() => {
            instructions.innerText = "Exhale Breath Slowly"

        },4000)
    }, 4000);

}

//  breathing app function
const breathingApp = () => {
    const breathingAnimation = setInterval(() => {
        if (breathsLeft === 0){
            clearInterval(breathingAnimation);
            instructions.innerText = "Breathing Session Completed. Click 'Start' to start another session!"
            start.classList.remove("button-inactive");
            breathsLeft = numberOfBreaths.value;
            breathsText.innerText = breathsLeft;
            return;
        }
        growCircle();
        breathTextUpdate(); 
    }, 12000)
}

// start breathing
start.addEventListener('click', () => {
    start.classList.add("button-inactive");
    instructions.innerText = "Relax yourself and get ready to starting breathing";
    setTimeout(() => {
    instructions.innerText = "Breathing is about to start...";
    setTimeout(() => {
          breathingApp();
          growCircle();
          breathTextUpdate();


    }, 2000)
    }, 2000)
});