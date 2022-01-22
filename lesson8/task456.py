class Storage:
    devices_total_stats = {}
    devices_data = {}

    @staticmethod
    def put_device_to_storage(device):
        if device.name in Storage.devices_data.keys():
            inner_model_list = Storage.devices_data[device.name]
            model_exists = False
            for item in inner_model_list:
                if item['model'] == device.model:
                    item['amount'] = item['amount'] + device.amount
                    model_exists = True
            if not model_exists:
                inner_model_list.append({'model': device.model, 'amount': device.amount})
        else:
            Storage.devices_data.update({device.name: [{'model': device.model, 'amount': device.amount}]})
        print(f'На склад поступил {device.name}, модель {device.model}, количество {device.amount}')

    @staticmethod
    def get_device_from_storage(device):
        if device.name in Storage.devices_data.keys():
            inner_model_list = Storage.devices_data[device.name]
            model_exists = False
            for item in inner_model_list:
                if item['model'] == device.model:
                    if item['amount'] - device.amount < 0:
                        print(f'На складе недостаточно запрашиваемых моделей {device.name} {device.model}')
                    else:
                        item['amount'] = item['amount'] - device.amount
                        print(f'В компанию отправлено {device.name} {device.model} количеством {device.amount} штук.')
                model_exists = True
            if not model_exists:
                print(f'Такой модели {device.name} {device.model} нет на складе')
        else:
            print(f'Техники {device.name} не осталось на складе')

    @staticmethod
    def get_storage_information():
        print('Количество оргтехники на складе:')
        print(Storage.devices_data)


class OfficeEquipment:

    def __init__(self, name, model, amount, paper_format, pages_per_minute):
        if type(amount) != int:
            raise TypeError
        self.name = name
        self.model = model
        self.amount = amount
        self.format = paper_format
        self.pages_per_minute = pages_per_minute


class Printer(OfficeEquipment):

    def __init__(self, model, amount, paper_format, pages_per_minute, color, technology, name='Printer'):
        super(Printer, self).__init__(name, model, amount, paper_format, pages_per_minute)
        self.color = color
        self.technology = technology


class Scanner(OfficeEquipment):

    def __init__(self, model, amount, paper_format, pages_per_minute, type, sensor_type, name='Scanner'):
        super(Scanner, self).__init__(name, model, amount, paper_format, pages_per_minute)
        self.type = type
        self.sensor_type = sensor_type


class Xerox(OfficeEquipment):

    def __init__(self, model, amount, paper_format, pages_per_minute, type, name='Xerox'):
        super(Xerox, self).__init__(name, model, amount, paper_format, pages_per_minute)
        self.type = type

    def get_description(self):
        return super().get_description().update({'Тип': self.type})


Storage.put_device_to_storage(Printer('Epson L-132', 12, 'A4', 25, 'чёрно-белый', 'лазерный'))
Storage.put_device_to_storage(Printer('Epson L-132', 4, 'A4', 25, 'чёрно-белый', 'лазерный'))
Storage.put_device_to_storage(Printer('Epson L-136', 8, 'A4', 20, 'цветной', 'лазерный'))
Storage.put_device_to_storage(Scanner('HP ScanJet 4500', 2, 'A4', 30, 'планшетный', 'CIS'))
Storage.put_device_to_storage(Scanner('HP ScanJet 4500', 1, 'A4', 30, 'планшетный', 'CIS'))
Storage.put_device_to_storage(Scanner('HP ScanJet 6500', 3, 'A4', 30, 'планшетный', 'CCD'))
print(Storage.get_storage_information())
Storage.get_device_from_storage(Xerox('Xerox 3020', 1, 'A4', 12, 'МФУ'))
Storage.get_device_from_storage(Printer('Epson L-132', 8, 'A4', 25, 'чёрно-белый', 'лазерный'))
Storage.get_device_from_storage(Printer('Epson L-136', 9, 'A4', 25, 'чёрно-белый', 'лазерный'))
print(Storage.get_storage_information())
