from src.IHM.src.components.communication.Enum.Inspetion_result import InspectionResult



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

