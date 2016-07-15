#!/usr/bin/python


# To support more units just add here the value in metres
SI_VALUES = {
    'm': 1,
    'yd': 1 / 1.0936,
    'in': 1 / 0.003937,
}


class UnitError(Exception):
    pass


class Conversor:
    @classmethod
    def convert(cls, from_unit, to_unit, value):
        if not all(unit in SI_VALUES for unit in [from_unit, to_unit]):
            raise UnitError('Unit not supported')
        new_value = float(value) * SI_VALUES[from_unit] / SI_VALUES[to_unit]
        return new_value, to_unit

    @classmethod
    def parse_str(cls, string):
        value, unit = string.split(' ')
        if unit not in SI_VALUES:
            raise UnitError('Unit not supported')
        return float(value), unit

    @classmethod
    def get_value_str(self, value, unit):
        if unit not in SI_VALUES:
            raise UnitError('Unit not supported')
        value = str(float(value))
        return ' '.join(value, unit)
