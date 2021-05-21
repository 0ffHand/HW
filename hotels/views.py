from django.shortcuts import render
from hotels.models import Room


def main_page(request):
    return render(request, "hotels/index.html")
