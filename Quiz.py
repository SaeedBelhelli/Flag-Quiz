var flags = getColumn("Countries and Territories", "Flag");
var countries = getColumn("Countries and Territories", "Country Name");

var currentCountryIndex = 0;
var score = 0;
var answerSubmitted = false;

function shuffleArray(array) {
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}

function shuffleCountriesAndFlags() {
    for (var i = countries.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var tempCountry = countries[i];
        countries[i] = countries[j];
        countries[j] = tempCountry;
        var tempFlag = flags[i];
        flags[i] = flags[j];
        flags[j] = tempFlag;
    }
    countries = countries.slice(0, 15);
    flags = flags.slice(0, 15);
}

function startQuiz() {
    shuffleCountriesAndFlags();
    currentCountryIndex = 0;
    score = 0;
    setText("score", score);
    answerSubmitted = false;
    displayCountry();
    setScreen("quizScreen");
}

function displayCountry() {
    setText("feedback", "");
    setProperty("flagImage", "image", flags[currentCountryIndex]);
    var options = [countries[currentCountryIndex]];
    while (options.length < 3) {
        var randomIndex = Math.floor(Math.random() * countries.length);
        var randomCountry = countries[randomIndex];
        if (options.indexOf(randomCountry) === -1) {
            options.push(randomCountry);
        }
    }
    shuffleArray(options);
    setProperty("countryOptionsDropdown", "options", options);
    setText("countryNumberLabel", "Country " + (currentCountryIndex + 1) + " of " + countries.length);
    answerSubmitted = false;
}

function checkAnswer(userAnswer) {
    if (userAnswer === countries[currentCountryIndex]) {
        score += 2;
        setText("score", score);
        setText("feedback", "Correct!");
    } else {
        setText("feedback", "Incorrect. The correct answer is " + countries[currentCountryIndex]);
    }
    updateScoreDisplay();
    answerSubmitted = true;
}

onEvent("submitAnswerButton", "click", function() {
    if (!answerSubmitted) {
        checkAnswer(getText("countryOptionsDropdown"));
        setTimeout(function() {
            currentCountryIndex++;
            if (currentCountryIndex < countries.length) {
                displayCountry();
            } else {
                setScreen("scoreScreen");
                updateScoreDisplay();
            }
        }, 1000);
    }
});

onEvent("submitLetterButton", "click", function() {
    var letter = getText("letterInput").toUpperCase();
    if (letter.length === 1 && letter.match(/[A-Z]/i)) {
        populateDropdownWithFilteredCountries(letter);
        setScreen("countrySelectionScreen");
        setText("letterInput", "");
        setProperty("flagDisplay", "image", "icon://fa-picture-o");
    } else {
        setText("letterInput", "");
        showElement("feedbackLabel");
        setText("feedbackLabel", "Please enter exactly one letter.");
        setTimeout(function() {
          hideElement("feedbackLabel");
        }, 1000);
    }
});

function populateDropdownWithFilteredCountries(letter) {
    var filteredCountries = countries.filter(function(country) {
        return country.substring(0, letter.length).toUpperCase() === letter.toUpperCase();
    });
    setProperty("countryDropdown", "options", filteredCountries);
}

onEvent("showFlagButton", "click", function() {
    var selectedCountry = getText("countryDropdown");
    var countryIndex = countries.indexOf(selectedCountry);
    var flagUrl = flags[countryIndex];
    setProperty("flagDisplay", "image", flagUrl);
});

function updateScoreDisplay() {
    setText("scoreDisplay", "Your Score: " + score);
}

onEvent("startQuizButton", "click", function() {
    startQuiz();
});

onEvent("restartButton", "click", function() {
    startQuiz();
});

onEvent("toHome", "click", function() {
    setScreen("welcomeScreen");
});

onEvent("learnMore", "click", function() {
    setScreen("searchScreen");
});

onEvent("backToSearch", "click", function() {
    setProperty("flagDisplay", "image", "icon://fa-picture-o");
    setScreen("searchScreen");
});

onEvent("backToWelcome", "click", function() {
    setScreen("welcomeScreen");
});

setScreen("welcomeScreen");
