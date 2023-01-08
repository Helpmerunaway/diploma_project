import json
from faker import Faker
import pytest
from pytest_voluptuous import S
import allure
from tests.web_api.data.data import dogz
from tests.web_api.utils.sessions import dog

faker = Faker()


@allure.feature('Random dog')
@allure.title('TEST: Negative. Get random dog image')
@pytest.mark.xfail(reason='error_404')
def test_negative_get_random_dog():
	response = dog().get('breeds/image/randome')

	with allure.step('Request sended, looking at the response code'):
		assert response.status_code == 404,\
			f"Wrong response code, received {response.status_code}"

	with allure.step('Checking response status'):
		response = response.json()
		print(response)
		assert response['status'] == 'error'


@allure.feature('Random dog breed afghan')
@allure.title('TEST: Negative. Get random dog image')
def test_single_random_image_from_afghan_collection():
	response = dog().get('breed/hound/afghan/images/random')
	with allure.step('Request sended, looking at the response code'):
		assert response.status_code == 200, \
			f"Wrong response code, received {response.status_code}"

	with allure.step('Checking response status'):
		response = response.json()
		assert response['status'] == 'success'
		assert 'hound-afghan' in response['message']
		assert S(dogz) == response


@allure.feature('Random dog')
@allure.title('TEST: Get random dog image')
def test_get_random_dog():
	response = dog().get('breeds/image/random')

	with allure.step('Request sended, looking at the response code'):
		assert response.status_code == 200,\
			f"Wrong response code, received {response.status_code}"

	with allure.step('Checking response status'):
		response = response.json()
		assert response['status'] == 'success'


@allure.feature('Random dog dingo')
@allure.title('TEST: Get random dog image breed dingo')
def test_get_random_dog_image_breed_dingo():
	response = dog().get('breed/dingo/images/random')
	with allure.step('Request sended, looking at the response code'):
		assert response.status_code == 200,\
				f"Wrong response code, received {response.status_code}"
	with allure.step('Checking response status'):
		response = response.json()
		assert response['status'] == 'success'
	with allure.step('Checking response message'):
		assert 'jpg' in response['message']


@allure.feature('Random dog')
@pytest.mark.parametrize("breed_terrier", [
    "american",
	"australian",
	"bedlington",
	"border",
	"cairn",
	"dandie",
	"fox",
	"irish",
	"kerryblue",
	"lakeland",
	"norfolk",
	"norwich",
	"patterdale",
	"russell",
	"scottish",
	"sealyham",
	"silky",
	"tibetan",
	"toy",
	"welsh",
	"westhighland",
	"wheaten",
	"yorkshire"
])
@allure.title('TEST: Image of a random dog from a terrier breed')
def test_get_random_terrier_breed_image(breed_terrier):
	response = dog().get(f'breed/terrier/{breed_terrier}/images/random')
	response = response.json()
	with allure.step('Request sended, looking at the response message'):
		assert breed_terrier in response["message"],\
			f"No link to the dog image, response = {response}"


@allure.feature('List of dog images')
@allure.title('TEST: List of all terrier dogs images contains only images')
@pytest.mark.parametrize("file", ['.doc', '.html', '.exe', '.txt'])
def test_get_breed_images_and_check_file_type(file):
	response = dog().get("breed/terrier/images")
	response = response.json()
	result = '\n'.join(response['message'])
	with allure.step('Request sended, looking at the file extension on response'):
		assert file not in result, \
			f"Founded file with the extension - {file}"


@allure.feature('List of dog images')
@pytest.mark.parametrize("breed", [
	"akita",
	"husky",
	"labrador",
	"pomeranian",
	"shiba",
	"australian",
	"collie",
	"corgi"
])
@allure.title('TEST: List of certain dog breed images')
def test_get_random_breed_images(breed):
	response = dog().get(f'breed/{breed}/images/')
	response = response.json()
	with allure.step('Request sended, looking at the response status'):
		assert response["status"] == 'success',\
			f'Something goes wrong status code is {response.status_code}'


@allure.feature('List of dog images')
@allure.title('TEST: List certain number of random images')
@pytest.mark.parametrize('number_of_images', [i for i in range(1, 10)])
def test_get_few_sub_breed_random_images(dog_api, number_of_images):
	response = dog_api.get(f"breed/terrier/norfolk/images/random/{number_of_images}")
	response = response.json()
	final_len = len(response["message"])
	with allure.step('Request sended, looking at the number of images'):
		assert final_len == number_of_images,\
			f"Wrong number of photo = {number_of_images}"
	with allure.step('Checking response status'):
		assert response["status"] == 'success', \
			f'Something goes wrong status code is {response.status_code}'