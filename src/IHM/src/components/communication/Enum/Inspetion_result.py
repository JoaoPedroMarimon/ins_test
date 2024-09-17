from enum import Enum


class InspectionResult(Enum):
    NAO_INSPECIONADO = 0
    APROVADO = {"background": "#00A336", "color": "cor: #fff"}
    REPROVADO = {"background": "#ff0000", "color": "cor: #fff"}

    @classmethod
    def convert_to_enum(cls, req) -> Enum:
        match req:
            case "aprovado":
                return InspectionResult.APROVADO
            case "reprovado":
                return InspectionResult.REPROVADO
            case "sem_inspecao":
                return InspectionResult.NAO_INSPECIONADO
