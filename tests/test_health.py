from unittest import mock

with mock.patch('redis.Redis'):
    import app as service


def test_KAN_27_AC2_health_returns_ok():
    client = service.app.test_client()
    resp = client.get('/health')
    assert resp.status_code == 200
    assert resp.get_json() == {'status': 'ok'}


def test_KAN_27_AC1_health_does_not_touch_redis():
    client = service.app.test_client()
    service.redis.reset_mock()
    client.get('/health')
    assert not service.redis.method_calls
