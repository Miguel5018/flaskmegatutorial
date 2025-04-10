from werkzeug.exceptions import HTTPException
from werkzeug.http import HTTP_STATUS_CODES

from app.api import bp


def bad_request(message):
    return error_response(400,message)


def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code,'Unknow error')}
    if message: 
        payload['message'] = message
        return payload, status_code
    

@bp.errorhandler(HTTPException)
def handle_exception(e):
    return error_response(e.code)