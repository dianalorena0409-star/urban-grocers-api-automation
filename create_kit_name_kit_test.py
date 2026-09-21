import data
import sender_stand_request

def get_kit_dody(kit_name):
    current_doby = data.kit_body.copy()
    current_doby['name'] = kit_name
    return current_doby

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()['authToken']

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201

def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

def test_1_kit_name_with_1_letter():
    new_kit_body = get_kit_dody('D')
    positive_assert(new_kit_body)

def test_2_kit_name_511_characters():
    new_kit_body = get_kit_dody('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')
    positive_assert(new_kit_body)

def test_3_kit_name_empty():
    new_kit_body = get_kit_dody('')
    negative_assert_code_400(new_kit_body)

def test_4_kit_name_512_characters():
    new_kit_body = get_kit_dody('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD')
    negative_assert_code_400(new_kit_body)

def test_5_kit_name_characters_specials():
    new_kit_body = get_kit_dody('№%@')
    positive_assert(new_kit_body)

def test_6_kit_name_space():
    new_kit_body = get_kit_dody('D iana')
    positive_assert(new_kit_body)

def test_7_kit_name_with_numbers():
    new_kit_body = get_kit_dody('1234')
    positive_assert(new_kit_body)

def test_8_kit_name_without_kit_value():
    new_kit_body = data.kit_body.copy()
    new_kit_body.pop('name')
    negative_assert_code_400(new_kit_body)

def test_9_kit_name_with_other_parameters():
    new_kit_body = get_kit_dody(1234)
    negative_assert_code_400(new_kit_body)








