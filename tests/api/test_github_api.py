import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 52
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0


#This part of the code was for independent study 
    #and was not part of the lecture material   
@pytest.mark.api
def test_emoji_list_not_empty(github_api):
    emojis_list = github_api.get_emojis_list()
    assert len(emojis_list) != 0


@pytest.mark.api
def test_commit_list_not_empty(github_api):
    commit_list = github_api.get_commit_list()
    assert len(commit_list) != 0


@pytest.mark.api
def test_first_commit_email(github_api):
    commit_list = github_api.get_commit_list()
    assert commit_list[0]['commit']['author']['email'] == 'kleunodlav@gmail.com'
