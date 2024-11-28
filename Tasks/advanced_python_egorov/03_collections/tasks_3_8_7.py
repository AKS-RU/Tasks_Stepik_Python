# Перед вами имеется список из 30 элементов класса Contact, созданных при помощи namedtuple

# Выведите информацию о людях в формате

# {name} - {email}
# в лексикографическом порядке номеров телефона ( в порядке увеличения цифр от 0 до 9)

# Сами телефоны состоят из 11 цифр, между которыми могут стоять символы дефис -, которые
# необходимо игнорировать при сортировке

from collections import namedtuple

Contact = namedtuple('Contact', ['name', 'phone_number', 'email'])

contacts = [Contact('John Smith', '123-456-7890', 'johnsmith@example.com'),
            Contact('Jane Doe', '098-7654321', 'janedoe@example.com'),
            Contact('Bob Jones', '456-789-0123', 'bobjones@example.com'),
            Contact('Alice White', '111222-3333', 'alicewhite@example.com'),
            Contact('David Green', '222-333-4444', 'davidgreen@example.com'),
            Contact('Michael Brown', '333-444-5555',
                    'michaelbrown@example.com'),
            Contact('Mark Wilson', '444-555-6666', 'markwilson@example.com'),
            Contact('Lisa Davis', '555-666-7777', 'lisadavis@example.com'),
            Contact('James Anderson', '666-777-8888',
                    'jamesanderson@example.com'),
            Contact('Daniel Taylor', '777-888-9999',
                    'danieltaylor@example.com'),
            Contact('Elizabeth Thomas', '888-999-0000',
                    'elizabeththomas@example.com'),
            Contact('Matthew Moore', '999-0001111',
                    'matthewmoore@example.com'),
            Contact('Jennifer Jackson', '000-111-2222',
                    'jenniferjackson@example.com'),
            Contact('William Taylor', '123-234-3456',
                    'williamtaylor@example.com'),
            Contact('Karen White', '2343454567', 'karenwhite@example.com'),
            Contact('Joseph Harris', '345456-5678',
                    'josephharris@example.com'),
            Contact('Charles Martin', '456-5676789',
                    'charlesmartin@example.com'),
            Contact('Thomas Thompson', '567-678-7890',
                    'thomasthompson@example.com'),
            Contact('Linda Garcia', '678-789-8901', 'lindagarcia@example.com'),
            Contact('Paul Robinson', '789-890-9012',
                    'paulrobinson@example.com'),
            Contact('Katherine Clark', '890901-0123',
                    'katherineclark@example.com'),
            Contact('Brian Lewis', '901-012-1234', 'brianlewis@example.com'),
            Contact('Rachel Walker', '012123-2345',
                    'rachelwalker@example.com'),
            Contact('Mark Anderson', '123-2343456',
                    'markanderson@example.com'),
            Contact('Steven Scott', '234-345-4567', 'stevenscott@example.com'),
            Contact('John Young', '345-4565678', 'johnyoung@example.com'),
            Contact('David Allen', '456-5676789', 'davidallen@example.com'),
            Contact('Richard Hernandez', '567678-7890',
                    'richardhernandez@example.com'),
            Contact('Jessica King', '678-789-8901', 'jessicaking@example.com'),
            Contact('Charles Brown', '789-890-9012',
                    'charlesbrown@example.com'),
            Contact('Margaret Miller', '890-9010123',
                    'margaretmiller@example.com'),
            Contact('William Davis', '901-012-1234', 'williamdavis@example.com')]


for name, _, email in sorted(contacts, key=lambda x: x[1].replace('-', '')):
    print(f'{name} - {email}')
