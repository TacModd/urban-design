from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
# from django.http import loader
from django.urls import reverse

from .models import Image, Galleries

# Create your views here.

def index(request):
	latest_galleries = Galleries.objects.order_by('-pub_date')[:5]
	template = loader.get_template('gallery/index.html')
	context = { 'latest_galleries': latest_galleries }
	# output = ', '.join([g.gallery_desc for g in latest_galleries])
	# return HttpResponse(template.render(context, request))
	return render(request, 'gallery/index.html', context)

def detail(request, gallery_id):
	'''
	try:
		gallery = Galleries.objects.get(pk=gallery_id)
	except Galleries.DoesNotExist:
		raise Http404("Gallery does not exist")
	'''
	gallery = get_object_or_404(Galleries, pk=gallery_id)
	# return HttpResponse("Gallery %s." % gallery_id)
	return render(request, 'gallery/detail.html', {'gallery': gallery} )

def results(request, gallery_id):
	question = get_object_or_404(Gallery, pk=gallery_id)
	return render(request, 'gallery/results.html', {gallery'': gallery})
	# return HttpResponse("Results for %s." % gallery_id)

def vote(request, gallery_id):
	gallery = get_object_or_404(Galleries, pk=gallery_id)
	try:
		selected_gallery = gallery.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Image.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'gallery/detail.html', {
			'image': image,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return a HttpResponseRedirect after successfully
		# dealing with POST data. This prevents data from being
		# posted twice if a user hits the Back button.
		return HttpResponseRedirect(reverse('gallery:results', args=(gallery.id,)))

