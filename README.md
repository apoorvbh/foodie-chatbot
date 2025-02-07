# foodie-chatbot

## Description:
The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. The project brief is as follows.

The bot takes the following inputs from the user:

### City: 
Take the input from the customer as a text field.

### Cuisine Preference: 
Take the cuisine preference from the customer. The bot should list out the following six cuisine categories (Chinese, Mexican, Italian, American, South Indian & North Indian) and the customer can select any one out of that.

### Average budget for two people: 
Segment the price range (average budget for two people) into three price categories: lesser than 300, 300 to 700 and more than 700. The bot should ask the user to select one of the three price categories.

While showing the results to the user, the bot displays the top 5 restaurants in a sorted order (descending) of the average Zomato user rating (on a scale of 1-5, 5 being the highest). 

Finally, the bot asks the user whether he/she wants the details of the top 10 restaurants on email. If the user replies 'yes', the bot asks for user’s email id and then send it over email. Else, just reply with a 'goodbye' message.

### Important Notes: 
Assumed that Bot works only in Tier-1 and Tier-2 cities. 
The bot is able to identify common synonyms of city names, such as Bangalore/Bengaluru, Mumbai/Bombay etc.
 
Chatbot provide results for tier-1 and tier-2 cities only, while for tier-3 cities, it replies back with something like "We do not operate in that area yet".

## Python Version used: 3.7.6

## Use following command for generating test results in project root folder:
rasa test --config config.yml --cross-validation --stories e2e_stories.md --e2e --out test_results

## Use following command to install below mentioned packages:
pip install -r requirements.txt

## Add following secrets in secrets.yml:
- zomato:user_key
- smtp:sender_email_id (gmail email id)
- smtp:sender_password

## Tested on following packages version:
- absl-py                  0.9.0
- aiofiles                 0.4.0
- aiohttp                  3.6.2
- alembic                  1.0.11
- APScheduler              3.6.3
- astor                    0.8.1
- astroid                  2.3.3
- async-generator          1.10
- async-timeout            3.0.1
- attrs                    19.3.0
- Automat                  0.8.0
- blinker                  1.4
- blis                     0.2.4
- boto3                    1.10.49
- botocore                 1.13.49
- bson                     0.5.8
- bz2file                  0.98
- cachetools               4.0.0
- certifi                  2019.11.28
- cffi                     1.13.2
- chardet                  3.0.4
- Click                    7.0
- cloudpickle              0.6.1
- colorama                 0.4.3
- colorclass               2.2.0
- coloredlogs              10.0
- colorhash                1.0.2
- ConfigArgParse           1.0
- constantly               15.1.0
- cryptography             2.8
- cycler                   0.10.0
- cymem                    2.0.3
- decorator                4.4.1
- dill                     0.3.1.1
- dnspython                1.16.0
- docopt                   0.6.2
- docutils                 0.15.2
- dopamine-rl              3.0.1
- en-core-web-md           2.1.0
- fbmessenger              6.0.0
- Flask                    1.1.1
- Flask-Mail               0.9.1
- future                   0.17.1
- gast                     0.2.2
- gevent                   1.4.0
- gin-config               0.3.0
- gitdb2                   2.0.6
- GitPython                3.0.5
- google-api-python-client 1.7.11
- google-auth              1.10.0
- google-auth-httplib2     0.0.3
- google-pasta             0.1.8
- googleapis-common-protos 1.6.0
- greenlet                 0.4.15
- grpcio                   1.26.0
- gunicorn                 20.0.4
- gym                      0.15.4
- h11                      0.8.1
- h2                       3.1.1
- h5py                     2.10.0
- hpack                    3.0.0
- httpcore                 0.3.0
- httplib2                 0.15.0
- httptools                0.0.13
- humanfriendly            4.18
- hyperframe               5.2.0
- hyperlink                19.0.0
- hyperopt                 0.1.1
- idna                     2.8
- importlib-metadata       1.3.0
- incremental              17.5.0
- isodate                  0.6.0
- isort                    4.3.21
- itsdangerous             1.1.0
- Jinja2                   2.10.3
- jmespath                 0.9.4
- jsonpickle               1.2
- jsonschema               3.2.0
- Keras-Applications       1.0.8
- Keras-Preprocessing      1.1.0
- kfac                     0.2.0
- kiwisolver               1.1.0
- klein                    17.10.0
- lazy-object-proxy        1.4.3
- Mako                     1.1.0
- Markdown                 3.1.1
- MarkupSafe               1.1.1
- matplotlib               3.1.2
- mattermostwrapper        2.1
- mccabe                   0.6.1
- mesh-tensorflow          0.1.9
- more-itertools           8.0.2
- mpmath                   1.1.0
- multidict                4.6.1
- murmurhash               1.0.2
- networkx                 2.3
- numpy                    1.18.1
- oauth2client             4.1.3
- opencv-python            4.1.2.30
- opt-einsum               3.1.0
- packaging                19.2
- pika                     1.0.1
- Pillow                   7.0.0
- pip                      19.3.1
- plac                     0.9.6
- preshed                  2.0.1
- promise                  2.3
- prompt-toolkit           2.0.10
- protobuf                 3.11.2
- pyasn1                   0.4.8
- pyasn1-modules           0.2.7
- pycparser                2.19
- pydot                    1.4.1
- pyglet                   1.3.2
- PyHamcrest               2.0.0
- PyJWT                    1.7.1
- pykwalify                1.7.0
- pylint                   2.4.4
- pymongo                  3.10.1
- pyparsing                2.4.6
- pypng                    0.0.20
- pyreadline               2.1
- pyrsistent               0.15.7
- python-crfsuite          0.9.6
- python-dateutil          2.8.1
- python-editor            1.0.4
- python-engineio          3.11.2
- python-socketio          4.4.0
- python-telegram-bot      11.1.0
- pytz                     2019.3
- PyYAML                   5.3
- questionary              1.4.0
- rasa                     1.6.1
- rasa-sdk                 1.6.1
- rasa-x                   0.24.1
- redis                    3.3.11
- requests                 2.22.0
- requests-async           0.5.0
- requests-toolbelt        0.9.1
- rfc3986                  1.3.2
- rocketchat-API           0.6.36
- rsa                      4.0
- ruamel.yaml              0.15.100
- s3transfer               0.2.1
- sanic                    19.9.0
- Sanic-Cors               0.9.9.post1
- sanic-jwt                1.4.0
- Sanic-Plugins-Framework  0.8.2.post1
- scikit-learn             0.20.4
- scipy                    1.4.1
- setuptools               44.0.0.post20200106
- setuptools-scm           3.3.3
- simplejson               3.17.0
- six                      1.13.0
- sklearn-crfsuite         0.3.6
- slackclient              1.3.2
- smmap2                   2.0.5
- spacy                    2.1.9
- SQLAlchemy               1.3.12
- srsly                    1.0.1
- sympy                    1.5.1
- tabulate                 0.8.6
- tensor2tensor            1.14.1
- tensorboard              1.15.0
- tensorflow               1.15.0
- tensorflow-datasets      1.3.2
- tensorflow-estimator     1.15.1
- tensorflow-gan           2.0.0
- tensorflow-gpu           1.15.0
- tensorflow-hub           0.7.0
- tensorflow-metadata      0.21.0
- tensorflow-probability   0.7.0
- termcolor                1.1.0
- terminaltables           3.1.0
- thinc                    7.0.8
- tqdm                     4.41.1
- twilio                   6.35.2
- Twisted                  19.10.0
- typed-ast                1.4.0
- typing                   3.7.4.1
- tzlocal                  2.0.0
- uritemplate              3.0.1
- urllib3                  1.25.7
- wasabi                   0.6.0
- wcwidth                  0.1.8
- webexteamssdk            1.2
- websocket-client         0.54.0
- websockets               8.1
- Werkzeug                 0.16.0
- wheel                    0.33.6
- wincertstore             0.2
- wrapt                    1.11.2
- yarl                     1.4.2
- zipp                     0.6.0
- zope.interface           4.7.1