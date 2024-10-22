from src.IHM.src.components.communication.Enum.Inspetion_result import InspectionResult



class MessageController:
    @classmethod
    def convert_result_to_enum(cls, req) -> InspectionResult:
        match req:
            case "approved":
                return InspectionResult.APROVADO
            case "reproved":
                return InspectionResult.REPROVADO
            case "no_inspection":
                return InspectionResult.NAO_INSPECIONADO

