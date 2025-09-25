def puntaje_equipo(datos_equipo): #dict[str, int | bool]
    """3*innovacion + presentacion - 1 si hubo errores."""
    return (
        3 * datos_equipo["innovacion"]
        + datos_equipo["presentacion"]
        - (1 if datos_equipo["errores"] else 0)
    )


def puntajes_ronda(ronda):
    """Devuelve {equipo: puntaje} para la ronda dada."""
    resultado = {}
    for equipo, datos_equipo in ronda.items():
        resultado[equipo] = puntaje_equipo(datos_equipo)
    return resultado


def mejor_equipo_ronda(ronda):
    """Devuelve (equipo_ganador, puntaje) del mejor en la ronda; desempate alfabético."""
    ps = puntajes_ronda(ronda)
    lista_puntajes = list(ps.items())

    mejor_equipo = None
    mejor_puntaje = -10**9

    for equipo, puntaje in lista_puntajes:
        if puntaje > mejor_puntaje or (puntaje == mejor_puntaje and equipo > mejor_equipo):
            mejor_equipo, mejor_puntaje = equipo, puntaje

    return mejor_equipo, mejor_puntaje


def inicializar_acumulado(equipos):
    """Crea {equipo: {'innovacion','presentacion','errores','mer','total'} en 0}."""
    base = {"innovacion": 0, "presentacion": 0, "errores": 0, "mer": 0, "total": 0}
    acumulado = {}
    for equipo in equipos:
        acumulado[equipo] = base.copy()
    return acumulado

#acumulado = {
 #   "EquipoA": {"innovacion": 0, "presentacion": 0, "errores": 0, "mer": 0, "total": 0},
  #  "EquipoB": {"innovacion": 0, "presentacion": 0, "errores": 0, "mer": 0, "total": 0},
#}


def asegurar_equipos(acumulado, ronda):
    """Asegura que todos los equipos de la ronda existan en el acumulado."""
    for equipo in ronda.keys():
        if equipo not in acumulado:
            acumulado[equipo] = {"innovacion": 0, "presentacion": 0, "errores": 0, "mer": 0, "total": 0}


def actualizar_innovacion_presentacion(acumulado, ronda):
    """Suma innovación y presentación de la ronda al acumulado."""
    asegurar_equipos(acumulado, ronda)
    for equipo, datos_equipo in ronda.items():
        acumulado[equipo]["innovacion"] += datos_equipo["innovacion"]
        acumulado[equipo]["presentacion"] += datos_equipo["presentacion"]
    return acumulado


def actualizar_acumulado(acumulado, ronda, equipo_mer):
    """Acumula innovación, presentación, errores y total; incrementa MER del ganador."""
    asegurar_equipos(acumulado, ronda)

    for equipo, datos_equipo in ronda.items():
        innov_r = datos_equipo["innovacion"]
        pres_r = datos_equipo["presentacion"]
        err_r = 1 if bool(datos_equipo["errores"]) else 0
        pts_r = puntaje_equipo(datos_equipo)

        acumulado[equipo]["innovacion"] += innov_r
        acumulado[equipo]["presentacion"] += pres_r
        acumulado[equipo]["errores"] += err_r
        acumulado[equipo]["total"] += pts_r

    if equipo_mer not in acumulado:
        acumulado[equipo_mer] = {"innovacion": 0, "presentacion": 0, "errores": 0, "mer": 0, "total": 0}
    acumulado[equipo_mer]["mer"] += 1

    return acumulado


def procesar_torneo(evaluaciones):
    """Procesa todas las rondas y devuelve el acumulado final."""
    conjuntos = [set(r.keys()) for r in evaluaciones]
    equipos_unicos = set()
    for c in conjuntos:
        equipos_unicos = equipos_unicos.union(c)

    acumulado = inicializar_acumulado(sorted(list(equipos_unicos)))

    for ronda in evaluaciones:
        equipo_ganador, _ = mejor_equipo_ronda(ronda)
        acumulado = actualizar_acumulado(acumulado, ronda, equipo_ganador)

    return acumulado
