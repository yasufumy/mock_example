from unittest import mock
from download.core import download


@mock.patch('download.core.open', new_callable=mock.mock_open)
@mock.patch('download.core.requests.get', autospec=True)
def test_download(mock_get, mock_open):
    url = 'https://example.com/sample.txt'
    mock_get.return_value.text = 'sample'
    download(url)
    mock_get.assert_called_once_with(url)
    mock_open.assert_called_once_with('sample.txt', 'w', encoding='utf-8')
