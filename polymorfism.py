from abc import ABC, abstractmethod


class PaymentType(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        ...


class CreditCard(PaymentType):
    def process_payment(self, amount: float) -> None:
        print(f'Processing credit card payment for ${amount}')


class Cash(PaymentType):
    def process_payment(self, amount: float) -> None:
        print(f'Processing cash payment for ${amount}')


class IOU(PaymentType):
    def process_payment(self, amount: float) -> None:
        print(f'Processing IOU payment for ${amount}')


def checkout(payment_type: PaymentType, amount: float) -> None:
    payment_type.process_payment(amount)


credit_card: PaymentType = CreditCard()
cash: PaymentType = Cash()
iou: PaymentType = IOU()

checkout(credit_card, 100)
checkout(cash, 50)
checkout(iou, 1000)
