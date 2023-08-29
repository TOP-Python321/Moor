from typing import Self


class ClassBuilder:
    """
    Класс предоставляет возможность формирования текста кода класса.
    """
    def __init__(self, class_name: str):
        """
        Инициализация объекта ClassBuilder.

        :param class_name: Имя класса.
        """
        self.class_name = class_name
        self.fields = []
        self.inst_attrs = []

    def add_cls_field(self, field_name: str, value: object) -> Self:
        """
        Добавляет поле класса со значением.

        :param field_name: Имя поля класса.
        :param value: Значение поля класса.
        :return: Объект ClassBuilder.
        """
        field = f"{field_name} = {repr(value)}"
        self.fields.append(field)
        return self

    def add_inst_attr(self, attr_name: str, value: object) -> Self:
        """
        Добавляет атрибут экземпляра класса со значением.

        :param attr_name: Имя атрибута экземпляра.
        :param value: Значение атрибута экземпляра.
        :return: Объект ClassBuilder
        """
        attr = f"self.{attr_name} = {repr(value)}"
        self.inst_attrs.append(attr)
        return self

    def __str__(self):
        """
        Возвращает строковое представление объекта ClassBuilder.
        """
        indent: str = ' ' * 4

        field_str: str = '\n'.join([f"{indent}{field}" for field in self.fields])
        if field_str:
            field_str = f"{field_str}\n\n"

        inst_attr_str: str = '\n'.join([f"{indent*2}{attr}" for attr in self.inst_attrs])
        if inst_attr_str:
            inst_attr_str = f"\n{inst_attr_str}"

        if not self.fields and not self.inst_attrs:
            return f"class {self.class_name}:\n{indent}pass"

        return f"class {self.class_name}:\n{field_str}{indent}def __init__(self):{inst_attr_str}"


# >>> cb = ClassBuilder('Test').add_cls_field('__protected', []).add_inst_attr('foo', 'bar')
# >>> print(cb)
# class Test:
#     __protected = []
#
#     def __init__(self):
#         self.foo = 'bar'
# >>>
# >>> cb = ClassBuilder('Person').add_inst_attr('name', '').add_inst_attr('age', 0)
# >>> print(cb)
# class Person:
#     def __init__(self):
#         self.name = ''
#         self.age = 0
# >>>
# >>> cb = ClassBuilder('Foo')
# >>> print(cb)
# class Foo:
#     pass
# >>>
# >>> cb = ClassBuilder('Test').add_cls_field('__protected', []).add_inst_attr('foo', 'bar')
# >>> cb.add_cls_field('__protected1', ())
# <__main__.ClassBuilder object at 0x00000205A5D55A90>
# >>>
# >>> print(cb)
# class Test:
#     __protected = []
#     __protected1 = ()
#
#     def __init__(self):
#         self.foo = 'bar'
