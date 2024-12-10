from typing import Final

# Comm
MESSAGE_DATA: Final = "data"
MESSAGE_CONTENT: Final = "content"
MESSAGE_INIT: Final = "initialised"
MESSAGE_ORIGIN: Final = "origin"
MESSAGE_METHOD: Final = "method"
MESSAGE_CONTENT_ID: Final = "msgId"
MESSAGE_CONTENT_TYPE: Final = "type"
MESSAGE_CONTENT_URL: Final = "url"
MESSAGE_CONTENT_ERROR: Final = "error"
MESSAGE_CONTENT_EXTRAS: Final = "extras"
MESSAGE_CONTENT_VALUES: Final = "values"
MESSAGE_CONTENT_SUCCESS: Final = "success"

MESSAGE_ERROR_MESSAGE: Final = "message"
MESSAGE_ERROR_AVAILABLE: Final = "available"

MESSAGE_EXTRAS_MESSAGE: Final = "message"

# Message types
MESSAGE_TYPE_DOWNLOAD: Final = "esasky_jupyter_download"


VERSION_WARNING_HTML: Final = """
    <div style="    background-color: #fff3cd;
    background-color: #fff3cd;
    color: #856404;
    border: 1px solid #ffeeba;
    border-radius: 5px;
    padding: 12px;
    margin: 10px 0;
    font-size: 16px;
    font-family: Arial, sans-serif;
    ">
        <strong>Warning:</strong> The ESASky server has been updated since your
        installation of pyESASky.
        </br></br>
        Some commands might malfunction. Please upgrade your installation if
        you experience any issues
        </br></br>
        To upgrade, run:
        </br>
        <code>$ pip install --upgrade pyesasky </code>
        </br>
    </div>
    """