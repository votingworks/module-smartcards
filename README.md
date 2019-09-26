# SmartCard Module

This web server component provides a web interface to a connected smartcard.

## Install Requisite Software

```
sudo add-apt-repository ppa:deadsnakes/ppa

sudo make install
make build
```

## Run Tests

Install dependencies you need

```
make install-dev-dependencies
```

and then run the tests

```
make test
```

With code coverage

```
make coverage
```

## Start the Development Server

```
make run
```

## Mock a Smart Card

You can run the service with a mocked smart card as follows:

```
MOCK_SHORT_VALUE="<short_value_json>" MOCK_LONG_VALUE_FILE="<path_to_file>" make run
```

If configuring with the `tests/electionSample.json` file (see Clerk example below), you may use all the following examples.

Note: timestamps (eg. `c`, `bp`, `uz`, etc.) are UTC Timestamps which are in seconds, not miliseconds.

### Clerk
```
MOCK_SHORT_VALUE="{\"t\":\"clerk\",\"h\":\"blah\"}" MOCK_LONG_VALUE_FILE="tests/electionSample.json" make run
```

### Poll Worker
```
MOCK_SHORT_VALUE="{\"t\":\"pollworker\",\"h\":\"blah\"}" make run
```

### Voter
`$(date +%s)` will interpolate the current unix time stamp in seconds as the value of `c`.

#### Newly Encoded Voter Card Ready to Vote

Note: To have an expired voter card, manually update the `c` value to be 60 minutes (in seconds) or more in the past.
```
MOCK_SHORT_VALUE="{\"t\":\"voter\",\"bs\":\"12\",\"pr\":\"23\",\"c\":$(date +%s)}" make run
```

#### Voter Card with Votes. Ready for VxPrint.
```
MOCK_SHORT_VALUE="{\"t\":\"voter\",\"bs\":\"12\",\"pr\":\"23\",\"c\":$(date +%s),\"v\":{\"102\":\"yes\",\"president\":[{\"id\":\"court-blumhardt\",\"name\":\"Daniel Court and Amy Blumhardt\",\"partyId\":\"2\"}],\"senator\":[{\"id\":\"hewetson\",\"name\":\"Heather Hewetson\",\"partyId\":\"3\"}],\"representative-district-6\":[{\"id\":\"tawney\",\"name\":\"Glen Tawney\",\"partyId\":\"3\"}],\"governor\":[{\"id\":\"abcock\",\"name\":\"Barbara Adcock\",\"partyId\":\"3\"}],\"lieutenant-governor\":[{\"id\":\"norberg\",\"name\":\"Chris Norberg\",\"partyId\":\"0\"}],\"question-a\":\"yes\"}}" make run
```

#### Printed Voter Card
Note: manually update the `bp` value.
```
MOCK_SHORT_VALUE="{\"bs\":\"12\",\"pr\":\"23\",\"t\":\"voter\",\"bp\":1569257753}" make run
```

#### Timeout Expired Voter Card
Note: manually update the `uz` value. In `VxPrint+Mark` mode, if this value is
within BMD's `RECENT_PRINT_EXPIRATION_SECONDS` (currently 60 seconds) then then
"Cast Instructions" page will be displayed.
```
MOCK_SHORT_VALUE="{\"bs\":\"12\",\"pr\":\"23\",\"t\":\"voter\",\"uz\":1560454860}" make run
```

#### Voter Card with Primary Election ballot style

Note: you will have to update `tests/electionSample.json` to contain `12D` and then load this election as an Admin.
```
MOCK_SHORT_VALUE="{\"t\":\"voter\",\"bs\":\"12D\",\"pr\":\"23\",\"c\":$(date +%s)}" make run
```
