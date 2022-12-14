from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton

contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='π± Contact',request_contact=True),
        ],
    ],resize_keyboard=True,
)
vaqt = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='(8:00-12:00)',callback_data='(8:00-12:00)'),
            InlineKeyboardButton(text='(13:00-17:00)',callback_data='(13:00-17:00)')
        ],
    ],resize_keyboard=True
)

true_false = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='β Ha',callback_data='β Ha'),
            InlineKeyboardButton(text='β Yo\'q',callback_data='β Yo\'q')
        ],
    ]

)

course = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='π Matematika'),
            KeyboardButton(text='πΊπΈ Ingliz tili')
        ],
        [
            KeyboardButton(text='π» IT')
        ],
    ],resize_keyboard=True
)

about_teach = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ingliz tili o\'qtuvchisi haqida',callback_data='english'),
            InlineKeyboardButton(text='Matematika o\'qtuvchisi haqida',callback_data='math'),
        ],
        [
            InlineKeyboardButton(text='IT o\'qtuvchisi haqida',callback_data='it'),
        ],
        [
            InlineKeyboardButton(text='Ortga',callback_data='back'),
        ]
    ]
)

ha_yuq = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='β Yes'),
            KeyboardButton(text='β No')
        ],
    ],resize_keyboard=True
)

tugat = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='β Ha'),
            KeyboardButton(text='β Yuq')
        ],
    ],resize_keyboard=True
)


bosh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='β Kurslarimizga yozilish'),
            KeyboardButton(text='π Rasmiy kanalimiz')

        ],
        [
            KeyboardButton(text='π 165-Maktab statistikasi'),
            KeyboardButton(text='π 131-Maktab statistikasi')

        ],
        [
            KeyboardButton(text='π Biz haqimizda'),
            KeyboardButton(text='π§ Tini sozlash')
        ],

    ],
    resize_keyboard=True
)