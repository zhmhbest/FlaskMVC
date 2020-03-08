import random

FIRST_NAMES = """
    赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许
    何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章
    云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳
    酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常
    乐于时傅皮卞齐康伍余元卜顾孟平黄和穆萧尹
    姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞
    熊纪舒屈项祝董梁杜阮蓝闵席季麻强贾路娄危
    江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍
    虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲邓
    郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁
    荀羊於惠甄麴家封芮羿储靳汲邴糜松井段富巫
    乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫
    宁仇栾暴甘钭厉戎祖武符刘景詹束龙叶幸司韶
    郜黎蓟薄印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙
    池乔阴郁胥能苍双闻莘党翟谭贡劳逄姬申扶堵
    冉宰郦雍舄璩桑桂濮牛寿通边扈燕冀郏浦尚农
    温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎
    戈廖庾终暨居衡步都耿满弘匡国文寇广禄阙东
    欧殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚
    那简饶空曾毋沙乜养鞠须丰巢关蒯相查後荆红
    游竺权逯盖益桓公""".strip().replace('\n', '').replace(' ', '')
FIRST_NAMES_SIZE = len(FIRST_NAMES)


def random_first_name():
    return FIRST_NAMES[random.randint(0, FIRST_NAMES_SIZE - 1)]


def random_hans():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x} {body:x}'
    return bytes.fromhex(val).decode('gb2312')


def random_name():
    buffer = []
    buffer.append(random_first_name())
    for i in range(random.randint(1, 2)):
        buffer.append(random_hans())
    return ''.join(buffer)


def random_gender():
    return random.randint(0, 1)


def random_date():
    from common.Time import DateTimeHelper
    return DateTimeHelper.after_current_datetime(days=-random.randint(100, 9000))


def random_phone():
    return random.randint(10000000000, 19999999999)
