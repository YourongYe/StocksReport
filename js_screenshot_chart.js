//https://stackoverflow.com/questions/32531881/retrieve-fully-populated-dynamic-content-with-phantomjs
//https://stackoverflow.com/questions/25288307/phantomjs-and-clicking-a-form-button
var system = require('system');
var OUT_PATH = "./out/";
var TICKER = "";
var LINK = "";
var IMAGE_NAME = "";

if (system.args.length > 1){
    TICKER = system.args[1];
    //https://uk.finance.yahoo.com/quote/AAPL/chart?p=AAPL
    LINK = "https://uk.finance.yahoo.com/quote/"+TICKER+"/chart?p="+TICKER;
    IMAGE_NAME = TICKER+".png";
    console.log("Processing ticker ["+TICKER+"]");
    console.log("Link ["+LINK+"]");
    console.log("Image name ["+IMAGE_NAME+"]")
} else {
    console.log("No ticker provided");
    phantom.exit();
}

var LOAD_IN_PROGRESS = false;
var STEP_INDEX = 0;
var page = require('webpage').create();

// Route "console.log()" calls from within the Page context to the main Phantom context (i.e. current "this")
page.onConsoleMessage = function(msg) {
    console.log(msg);
};

page.onAlert = function(msg) {
    console.log('alert!!> ' + msg);
};

page.onLoadStarted = function() {
    LOAD_IN_PROGRESS = true;
    console.log("load started");
};

page.onLoadFinished = function(status) {
    LOAD_IN_PROGRESS = false;
    if (status !== 'success') {
        console.log('Unable to access network');
        phantom.exit();
    } else {
        console.log("load finished");
    }
};

var steps = [
             function() {
                 console.log("Opening page ["+LINK+"]");
                 page.open(LINK);
             },

             function() {
                 console.log("Clicking button");
                 //click 1 month
                 page.evaluate(function() {
                         var buttons = document.getElementsByTagName("button");
                         var search_text = "1D";
                         var found_button;

                         for (var i = 0; i < buttons.length; i++) {
                             if (buttons[i].textContent == search_text) {
                                 found_button = buttons[i];
                                 break;
                             }
                         }
                         if(found_button){
                             found_button.click();
                         }
                     });
             },


             function() {
                 console.log("Rendering image ["+IMAGE_NAME+"]");
                 page.render(OUT_PATH+IMAGE_NAME);
             }
             ];

interval = setInterval(function() {
        if (!LOAD_IN_PROGRESS && typeof steps[STEP_INDEX] == "function") {
            console.log("step " + (STEP_INDEX + 1));
            steps[STEP_INDEX]();
            STEP_INDEX++;
        }
        if (typeof steps[STEP_INDEX] != "function") {
            console.log("All done!");
            phantom.exit();
        }
    }, 10000);//wait for page rendering