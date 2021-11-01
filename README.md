# Sliide News App Testing

## Manual Tests
Issues are located at the [Issues](Issues) Folder.

## Automation Tests
Automation tests uses [uiautomator](https://github.com/xiaocong/uiautomator) library and standard python unit test framework library, as I am comfortable in Python based UI Auotmation. They are located in the following files:  
* [login_test.py](tests/system/login_test.py)
* [news_test.py](tests/system/news_test.py)

## Running Tests:
### Prerequisites
* Python 3
* Android SDK

1. Connect an Android Device with the App installed from source: https://github.com/sliide/technical_task_qa
2. Clone this repository.  
    ```bash
    git clone https://github.com/maragatham/sliide-news-system-tests
    cd sliide-news-system-tests
    ```
3. Populate Environment variables.
    ```bash
    export ANDROID_HOME=<path-to-android-sdk>
    ```
4. Install requirements and Excecute tests.
   ```bash
   pip install -r requirements.txt
   python -m unittest discover -s tests -p '*_test.py'
   ```

