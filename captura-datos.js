var someObject = {};
var jsonObjects = [];
var jsonString = "";

var n;
var COORD_AX;
var COORD_AY;
var COORD_BX;
var COORD_BY;

function showADialog(e){
    var confirmationMessage = '¿Seguro desea salir de la página?';
    //some of the older browsers require you to set the return value of the event
    (e || window.event).returnValue = confirmationMessage;     // Gecko and Trident
    return confirmationMessage;                                // Gecko and WebKit
}

window.addEventListener('beforeunload', function (e) {
	// Cancel the event
	//e.preventDefault(); // If you prevent default behavior in Mozilla Firefox prompt will always be shown
	// Chrome requires returnValue to be set
	//e.returnValue = '';
	jsonString = JSON.stringify(jsonObjects);
	console.log(jsonString)

	postAppletData('http://localhost:8080/applet01/', jsonObjects)
		.then(data => {
			console.log(`respuesta: ${JSON.stringify(data)}`);
		});

	var delayInMilliseconds = 5000; //5 seconds

	setTimeout(function () {
		//your code to be executed after 1 second
		console.log('Executed')
	}, delayInMilliseconds);
	
	//To show a dialog (uncomment to test):
    return showADialog(e);
});

async function postAppletData(url = '', data = {}) {
	// fetch('http://localhost:8080/applet01/', { method: 'POST' })
	// 	.then(function (response) {
	// 		if (response.ok) {
	// 			console.log('Applet01 was recorded');
	// 			return;
	// 		}
	// 		throw new Error('Request to Applet01 failed.');
	// 	})
	// 	.catch(function (error) {
	// 		console.log(error);
	// 	});


	let myHeaders = new Headers();
	// 'Content-Type': 'application/x-www-form-urlencoded',
	// 'Content-Type', 'image/jpeg'
	myHeaders.append('Content-Type', 'application/json');

	// Default options are marked with *
	const myInit = {
		method: 'POST',  // *GET, POST, PUT, DELETE, etc.
		mode: 'cors', // no-cors, *cors, same-origin
		cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
		credentials: 'same-origin', // include, *same-origin, omit
		headers: myHeaders,
		redirect: 'follow', // manual, *follow, error
		referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
		body: JSON.stringify(data) // body data type must match "Content-Type" header
	};

	let myRequest = new Request(url, myInit);

	const response = await fetch(myRequest);

	return response.json(); // parses JSON response into native JavaScript objects
}

function ggbOnInit(param) {
	document.ggbApplet.registerObjectUpdateListener("n", "updateElementListenerFunction");
}

function updateElementListenerFunction() {
	COORD_AX = ggbApplet.getXcoord("A");
	COORD_AY = ggbApplet.getYcoord("A");

	COORD_BX = ggbApplet.getXcoord("B");
	COORD_BY = ggbApplet.getYcoord("B");

	var n = ggbApplet.getValue("n");

	someObject = {
		puntoA: {
			x: COORD_AX,
			y: COORD_AY
		},
		puntoB: {
			x: COORD_BX,
			y: COORD_BY
		},
		numeroPasos: n
	};

	jsonObjects.push(someObject);
}