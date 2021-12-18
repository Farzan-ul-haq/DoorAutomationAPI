from core.models import Door
def get_door(id):
    return Door.objects.get(id=id)