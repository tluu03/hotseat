# hotseat

Below you have instructions on setting up hotseat.

## Up and running

First, install dependencies. The back-end is a simple Flask API, so you'll
probably want to set up a virtual environment as well. These commands assume
that you have [Python3](https://www.python.org/downloads/) and
[Node.js](https://nodejs.org/en/) (with npm) installed.

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
npm install
```

Now that you have everything installed, you can build and run the app with one
npm `run-script` command:

```
npm run app
```

This will compile the JavaScript modules and Less and start up the Flask API.

## Running tests

To run the tests, use the following commands. The first runs the Mocha
test-suite for the JavaScript app. The second runs the Python unit tests for the
API.

```
npm run test
python app/tests/<testFile>.py
```

You can also run the JavaScript tests in watch mode by passing an additional
flag into the npm `run-script` command.

```
npm run test -- -w
```

This enables that TDD sweetness, allowing you to focus on feeding the
red-to-green beast.

## Building individual pieces

There are also some npm scripts to make working with the JavaScript app nicer.
These include compiling the app:

```
npm run compile
```

setting up watch-servers to re-compile the JS/CSS when you save changes:

```
npm run watch
```

building the production version of the app:

```
npm run prod
```

Under the hood, these are just aliases for gulp tasks, so pop open `gulpfile.js`
if you want to see what's going on.
