import httpx
from core.log import logger
from core.config import settings

from requests.exceptions import HTTPError

def get_image(name: str = None):

    try:
        url = settings.external_image_api

        with httpx.Client() as client:
            response = client.get(url, params={'name': name})
            response.raise_for_status()
    except httpx.RequestError as exc:
        logger.error(f"An error occured while requesting {exc.request.url!r}.")
        return {
            "name": "error",
            "detail": f"An error occured while requesting {exc.request.url!r}.",
        }
    except httpx.HTTPStatusError as exc:
        logger.error(
            f"Error response {exc.response.status_code} while requesting {exc.request.url!r}."
        )
        return {"name": "error", "detail": exc}
    else:
        try:
            json_object = response.json()
            if 'image' in json_object:
                return {'image': json_object['image']}
            else:
                raise ValueError
        except ValueError as e:
            logger.info("Not Valid JSON")
            return {"name": "error", "detail": "Not Valid JSON"}
