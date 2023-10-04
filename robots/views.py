from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Robot
import json


@method_decorator(csrf_exempt, name='dispatch')
class PostRobotView(View):
    def post(self, request):
        post_body = json.loads(request.body)
        robot_version = post_body.get('version')
        robot_model = post_body.get('model')
        data = post_body.get('created')
        robot = {
            'model': robot_model,
            'version': robot_version,
            'serial': f'{robot_model}-{robot_version}',
            'created': data,
        }
        robot_obj = Robot.objects.create(**robot)
        data = {
            'message': f'New robot has been created with id {robot_obj.id}'
        }
        return JsonResponse(data, status=201)
