from src.IHM.src.components.communication.Enum.Inspetion_result import InspectionResult

from src.IHM.src.components.communication.Enum.Inspection_order import InspectionOrder


class MessageController:
    @classmethod
    def convert_result_to_enum(cls, req) -> InspectionResult:
        match req:
            case "aprovado":
                return InspectionResult.APROVADO
            case "reprovado":
                return InspectionResult.REPROVADO
            case "sem_inspecao":
                return InspectionResult.NAO_INSPECIONADO

    @classmethod
    def convert_order_to_enum(cls, req) -> InspectionOrder:
        match req:
            case "model":
                return InspectionOrder.GET_MODEL

    @classmethod
    def convert_to_enum(cls, req: str) -> InspectionOrder | InspectionResult:
        classification: str = req.split("-")[0]
        requisition: str = req.split("-")[1]
        match classification:
            case "order":
                return cls.convert_order_to_enum(requisition)

            case 'result':
                return cls.convert_result_to_enum(requisition)
