import httpx
from core.log import logger
from core.config import settings
from pydantic import BaseModel
from typing import Optional
from requests.exceptions import HTTPError

class Image(BaseModel):
    image: Optional[str]
    name: Optional[str] = None
    detail: Optional[str] = None

def get_image_simple(name):

    try:
        url = settings.external_image_api

        with httpx.Client() as client:
            
            logger.debug("URL: " + url)
            logger.debug("Name: " + name)

            response = client.get(url, params={'name': name})
            response.raise_for_status()
        try:
            json_object = response.json()
            if 'image' in json_object:
                return {'image': json_object['image']}
            else:
                raise ValueError
        except ValueError as e:
            error_msg = "Not Valid JSON"
            logger.error(error_msg)
            return Image(name='error', Image=error_msg)

    except httpx.RequestError as exc:
        error_msg = f"An error occured while requesting {exc.request.url!r}."
        logger.error(error_msg)
        return Image(name='error', Image=error_msg)

    except httpx.HTTPStatusError as exc:
        error_msg = f"Error response {exc.response.status_code} while requesting {exc.request.url!r}."
        logger.error(error_msg)
        return Image(name='error', Image=error_msg)

    except httpx.HTTPError as exc:
        error_msg = f"HTTPError Error while requesting {exc.request.url!r}."
        logger.error(error_msg)
        return Image(name='error', Image=error_msg)

    except httpx.InvalidURL as exc:
        error_msg = f"Error while requesting {exc.request.url!r}."
        logger.error(error_msg)
        return Image(name='error', Image=error_msg)

def get_image_simple_api_v2(name):

    try:
        url = settings.external_image_api

        with httpx.Client() as client:
            
            logger.debug("URL: " + url)
            logger.debug("Name: " + name)

            response = client.get(url, params={'author': name})
            response.raise_for_status()
        try:
            json_object = response.json()
            if 'image' in json_object:
                return {'image': json_object['image']}
            else:
                raise ValueError
        except ValueError as e:
            error_msg = "Not Valid JSON"
            logger.error(error_msg)
            return Image(name='error', Image=error_msg)

    except httpx.RequestError as exc:
        error_msg = f"An error occured while requesting {exc.request.url!r}."
        logger.error(error_msg)
        return Image(name='error', Image=error_msg)

    except httpx.HTTPStatusError as exc:
        error_msg = f"Error response {exc.response.status_code} while requesting {exc.request.url!r}."
        logger.error(error_msg)
        return Image(name='error', Image=error_msg)

    except httpx.HTTPError as exc:
        error_msg = f"HTTPError Error while requesting {exc.request.url!r}."
        logger.error(error_msg)
        return Image(name='error', Image=error_msg)

    except httpx.InvalidURL as exc:
        error_msg = f"Error while requesting {exc.request.url!r}."
        logger.error(error_msg)
        return Image(name='error', Image=error_msg)
