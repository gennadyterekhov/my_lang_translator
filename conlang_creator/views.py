from django.shortcuts import render, get_object_or_404
from user.models import User

from conlang_creator.models import Conlang
from phonology.models import Place, Manner, Consonant, Vowel, VowelHorizontalPosition, VowelVerticalPosition, Roundedness, Length

def create(request):
    title = 'Conlang creator'
    template = 'conlang_creator/create.html'

    places = Place.objects.all()
    manners = Manner.objects.all()
    consonants = Consonant.objects.all()

    vowels = Vowel.objects.all()
    horizontals = VowelHorizontalPosition.objects.all()
    verticals = VowelVerticalPosition.objects.all()
    roundednesses = Roundedness.objects.all()
    lengths = Length.objects.all()
    # print(vowels)
    # print(horizontals)
    # print(verticals)
    # print(roundednesses)
    # print(lengths)


    user = get_object_or_404(User, pk=request.session['user_id'])
    context = {
        'title': title,
        'user': user,
        'places': places,
        'manners': manners,
        'consonants': consonants,
        'vowels': vowels,
        'horizontals': horizontals,
        'verticals': verticals,
        'roundednesses': roundednesses,
        'lengths': lengths
        }
    return render(request, template, context)

def create_check(request):
    title = 'Conlang profile'

    user = get_object_or_404(User, pk=request.session['user_id'])

    original_name = request.POST.get('original_name', False)
    english_name = request.POST.get('english_name', False)
    description = request.POST.get('description', False)

    consonants = request.POST.get('consonants', False)
    vowels = request.POST.get('vowels', False)

    syllable_structure = request.POST.get('syllable_structure', False)
    word_structure = request.POST.get('word_structure', False)

    consonants_objects = []
    # так было на старой Бд
    # for con in consonants.split(' '):
    #     con_obj = Consonant.objects.filter(ipa=con)[0]
    #     consonants_objects.append(con_obj)
    # vowels_objects = []
    # for vow in vowels.split(' '):
    #     vow_obj = Vowel.objects.filter(ipa=vow)[0]
    #     vowels_objects.append(vow_obj)



    conlang = Conlang.objects.create(
        original_name=original_name,
        english_name=english_name,
        description=description,
        user=user,
        consonants=consonants,
        vowels=vowels,
        syllable_structure=syllable_structure,
        word_structure=word_structure
        )
    # consonants=consonants_objects, vowels=vowels_objects

    # на старой бд
    # conlang.consonants.set(consonants_objects)
    # conlang.vowels.set(vowels_objects)


    template = 'conlang_creator/profile.html'
    context = {'title': title, 'user': user, 'conlang': conlang}
    return render(request, template, context)


def profile(request, conlang_id):
    user = get_object_or_404(User, pk=request.session['user_id'])
    conlang = get_object_or_404(Conlang, pk=conlang_id)


    # на старой БД
    # consonants = conlang.consonants.all()
    # vowels = conlang.vowels.all()

    consonants = conlang.consonants.split(' ')
    vowels = conlang.vowels.split(' ')


    words_1 = []
    words_2 = []
    for c in consonants:
        for v in vowels:
            word = c + v
            words_1.append(word)
            for c2 in consonants:
                for v2 in vowels:
                    word = c + v + c2 + v2
                    words_2.append(word)
    


    title = 'Conlang profile'
    template = 'conlang_creator/profile.html'
    context = {'title': title, 'user': user, 'conlang': conlang, 'consonants': consonants, 'vowels': vowels, 'words_1': words_1, 'words_2': words_2}
    return render(request, template, context)

# <a href="{% url 'conlang_creator:profile' conlang.id %}">{{ conlang.english_name }}</a>
def conlang_list(request):
    user = get_object_or_404(User, pk=request.session['user_id'])
    conlangs = Conlang.objects.all()
    # conlangs = []
    # for conlang in all_conlangs:
    #     temp_user = get_object_or_404(User, pk=conlang.user_id)
    #     temp = {
    #         'original_name': conlang.original_name,
    #         'english_name': conlang.english_name,
    #         'description': conlang.description,
    #         'user_name': temp_user.name,
    #         'user_email': temp_user.email,
    #         }
    #     conlangs.append(temp)
    title = 'Conlang list'
    template = 'conlang_creator/list.html'
    context = {'title': title, 'user': user, 'conlangs': conlangs}
    return render(request, template, context)
