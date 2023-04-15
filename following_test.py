import twint

c = twint.Config()
c.Username = "NASAHubble"
c.Store_object = True
c.User_full = True

c.Graphql_id = 'b22I8WSfQ8H4Ev8486xAlQ'

twint.run.Lookup(c)
id = twint.output.users_list[0].id
following = twint.output.users_list[0].following
followers = twint.output.users_list[0].followers

c.Username = id

cookie = {
    '_twitter_sess': "BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%0ASGFzaHsABjoKQHVzZWR7ADoHaWQiJWFhMjcyZDc5NjgwYjk3ZTg3ZWI5MDdl%0AYzdjODQxOWZjOg9jcmVhdGVkX2F0bCsIomcsgYcBOgxjc3JmX2lkIiU1NDg0%0AZmE2MjVhYjMyNTNmZWVhNzAwODkzNzIxZDgwNQ%3D%3D--b8ecce19ba1b923b828014f556fc52578f9b6840",
    'att': "1-EIm71pKCYlXwqZ5g0tlLT6ExCXDDwaq2Oj19kt53",
    'auth_token': "4fe3ac7d1c471839a8f96b920afb202c1dc402e4",
    'ct0': "644e3593bc6cca39367a8b9496769559af85485edcabe1940e25237c0096f6db8acc6cff4b7191144f2eec27b805481e47adf97d0b174a7abf0faad90b28357415ad8cc68bdd1b4a35bab3573c62ed5f",
    'g_state': {"i_p":1681506052214,"i_l":1},
    'guest_id': "v1:168149884812032684",
    'guest_id_ads': "v1:168149884812032684",
    'guest_id_marketing':	"v1:168149884812032684",
    'kdt':	"G45IcMkN90UcRsdoIlLW1JzHEZnR5cnJnnk1IVaW",
    'lang':	"en",
    'personalization_id':	'"v1_YoUHVXZTT8vqkrxhWQKXqg=="',
    'twid':	"u=1646954433958346755"
}

c.Cookies = cookie

print('About to perform Following')

twint.run.Following(c)