from enum import Enum


class InspectionResult(Enum):

    NAO_INSPECIONADO = 0
    APROVADO = {"background": "#00A336", "color": "cor: #fff"}
    REPROVADO = {"background": "#ff0000", "color": "cor: #fff"}

    @classmethod
    def convert_to_enum(cls, req) -> Enum:
        match req:
            case "approved":
                return InspectionResult.APROVADO
            case "reproved":
                return InspectionResult.REPROVADO
            case "no_inspection":
                return InspectionResult.NAO_INSPECIONADO
