from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorControler

class TagCreatorView:
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        tag_creator_controller = TagCreatorControler()
        body = http_request.body
        product_code = body['product_code']
        response = tag_creator_controller.create(product_code)
        return HttpResponse(status_code=201, body=response)
