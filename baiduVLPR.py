from aip import AipOcr
from utils import api_setting


def get_vlpr(pic):
    ''' 车牌识别
    ======
    如果加入参数，可以这样

        >>> options = {}
        >>> options["multi_detect"] = "true"
        >>> return client.licensePlate(image, options)
    '''
    client = AipOcr(
        api_setting['appid'],
        api_setting['AK'],
        api_setting['SK'],
    )
    with open(pic, 'rb') as fp:
        image = fp.read()
    return client.licensePlate(image)


if __name__ == '__main__':
    print(get_vlpr('./th.jpg'))
