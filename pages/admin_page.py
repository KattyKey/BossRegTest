import requests
import re


class WorkWithAdminPage():

    def login_to_admin(self, admin_user_login, admin_user_password):
        sign_in_url = "https://dev.admin.slotoboss.com/platform/user/admin/auth/sign-in"
        sign_in_payload = "{\"login\":\"" + admin_user_login + "\",\"password\":\"" + admin_user_password + "\"}"
        sign_in_headers = {'Content-Type': 'application/json; charset=UTF-8'}
        authorize = requests.request("POST", sign_in_url, headers=sign_in_headers, data=sign_in_payload)
        query_id = re.search(r'id\":\"\d{5,6}', authorize.text)
        admin_user_id = re.findall('[0-9]+', query_id.group())[0]
        return ([authorize.headers['Access-Token'], str(admin_user_id)])

    def switch_user_to_test(self, admin_user_login, admin_user_password, user_email):
        user_id = str(self.find_userID_by_email(admin_user_login, admin_user_password, user_email))
        token_id_pair = self.login_to_admin(admin_user_login, admin_user_password)

        make_user_test_url = "https://dev.admin.slotoboss.com/platform/user/admin/players/change-user-is-test"
        make_user_test_payload = "{ \"id\": \"" + user_id + "\" }"
        make_user_test_headers = {'Token-Type': "Bearer", 'Access-Token': token_id_pair[0], 'uid': token_id_pair[1],
                                  'Content-Type': 'application/json; charset=UTF-8', 'client': 'user'}
        make_user_test_result = requests.request("POST", make_user_test_url, headers=make_user_test_headers,
                                                   data=make_user_test_payload)
        print(make_user_test_result.json())

    def find_userID_by_email(self, admin_user_login, admin_user_password, user_email):
        token_id_pair = self.login_to_admin(admin_user_login, admin_user_password)
        find_user_url = "https://dev.admin.slotoboss.com/platform/user/admin/players/find"
        find_user_payload = "{\"account\": { \"lastLogin\": {},\"dateRegistered\": {},\"firstDepositDate\": {} },\"client\": {\"email\": {\"flag\": \"like\", \"value\": \"" + user_email + "\"}},\"flags\": {\"withTestUsers\": true}}"
        find_user_headers = {'Token-Type': "Bearer", 'Access-Token': token_id_pair[0], 'uid': token_id_pair[1],
                             'Content-Type': 'application/json; charset=UTF-8', 'client': 'user'}
        user_result = requests.request("POST", find_user_url, headers=find_user_headers, data=find_user_payload)
        query_id = re.search(r'id\":\"\d{5,6}', user_result.text)
        user_id = re.findall('[0-9]+', query_id.group())[0]
        return user_id
