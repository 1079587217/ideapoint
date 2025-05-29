import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def get_cookies():
    chrome_options = Options()
    chrome_options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0")
    chrome_options.add_argument("--headless")

    # 创建 WebDriver 实例
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    # 访问要登录的页面
    driver.get("https://www.goofish.com")
    cookies = []
    _m_h5_tk=''
    _m_h5_tk_enc=''
    while driver.get_cookies() == []:
        cookies = driver.get_cookies()

    for cookie in cookies:
        if cookie['name'] == '_m_h5_tk':
            _m_h5_tk =cookie['value']
        if cookie['name'] == '_m_h5_tk_enc':
            _m_h5_tk_enc =cookie['value']
    driver.close()
    # print(_m_h5_tk)
    cookies = {
        'cookie2': '15537b6c6bb2dfed9bb9cd558696c7ab',
        'cna': '1+W+INmRhxcCAXWTGzhryqvL',
        'xlly_s': '1',
        'mtop_partitioned_detect': '1',
        '_m_h5_tk': _m_h5_tk,
        '_m_h5_tk_enc': _m_h5_tk_enc,
        'tfstk': 'gfmIZej4R6fQayqRFyvNf6Oi_7Z7Vd-VVTw-nYIFekEdw_HY_XPUYLx7wXVZYWkUv90igxIEYeqPVkqu2IR20nJnKuq-AajS2w2Tn--PwyLaX5FXTiR20nkpJJqrBIoP25OQ18E8pzURWdw3U_E8J8F9C8eP9aIKwd9_FJedw7Ud6AeUnuF-wyp_X8PTpuUKwAhPgtwWRWDBLwY8zyYNEvV12gn_BQVjdUjuBceBiSDQ1QOEfm4QMvF12BHFbGP7smdw5AcjJXyiNnO_DqcsVrEWAs2IWxZTToLf5kMZtmZKcBsUQlVUk4U6pHH_AWa0CrKytkg-t0anRTvmBkhioS4pSC2sYmz7iP199Ak_9rgSTCj8TqMt1roN_irxofi7koIzxiPjUE_5Crj7CSJ6CabuUSf-L0GiwaaLIJawCd1KryegC-J6CaXuJR2wCd91uI5..',
    }
    return cookies