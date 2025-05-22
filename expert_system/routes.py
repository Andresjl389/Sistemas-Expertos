def ruta_dificultad_respirar(respuestas):
    # Si no has respondido sobre dificultad para respirar, pregunta primero
    if 'dificultad_respirar' not in respuestas:
        return "¿Tienes dificultad para respirar? (yes/no)"
    
    dificultad = respuestas['dificultad_respirar']

    # Si dificultad es False, seguimos con otras preguntas (no retorno aquí)
    if dificultad is False:
        # Aquí empieza el camino alternativo para quienes NO tienen dificultad para respirar
        # Puedes poner preguntas para evaluar otros síntomas

        # Ejemplo simplificado: pregunta fatiga
        if 'fatiga' not in respuestas:
            return "¿Sientes fatiga? (yes/no)"
        
        fatiga = respuestas['fatiga']
        if fatiga:
            # Pregunta siguiente o diagnóstico según tu árbol
            if 'hinchazon_extremidades' not in respuestas:
                return "¿Tienes hinchazón en las extremidades? (yes/no)"
            
            if respuestas.get('hinchazon_extremidades'):
                return "Diagnóstico probable: Insuficiencia cardíaca leve."
            else:
                return "Diagnóstico probable: Fatiga general - evaluar con médico."

        else:
            # Si no fatiga
            if 'tos' not in respuestas:
                return "¿Tienes tos? (yes/no)"
            
            if respuestas.get('tos'):
                return "Diagnóstico probable: Tos leve - evaluar evolución."
            else:
                return "Diagnóstico probable: No hay síntomas relevantes detectados."

    # Si dificultad es True, seguimos con el camino para dificultad respiratoria
    if dificultad:  
        if 'dolor_pecho' not in respuestas:
            return "¿Sientes dolor en el pecho? (yes/no)"
        
        dolor_pecho = respuestas['dolor_pecho']
        if dolor_pecho:
            if 'dolor_brazo_izquierdo' not in respuestas:
                return "¿Tienes dolor en el brazo izquierdo? (yes/no)"
            if respuestas.get('dolor_brazo_izquierdo'):
                return "Diagnóstico probable: Pre-infarto."
            
            if 'dolor_esfuerzo' not in respuestas:
                return "¿El dolor empeora con esfuerzo? (yes/no)"
            if respuestas.get('dolor_esfuerzo'):
                return "Diagnóstico probable: Insuficiencia cardíaca."
            
            if 'tos_persistente' not in respuestas:
                return "¿Tienes tos persistente? (yes/no)"
            tos = respuestas.get('tos_persistente')
            
            if tos:
                if 'fiebre' not in respuestas:
                    return "¿Tienes fiebre? (yes/no)"
                if respuestas.get('fiebre'):
                    return "Diagnóstico probable: Neumonía."
                else:
                    return "Diagnóstico probable: Bronquitis."
            else:  # tos persistente = no
                if 'latidos_irregulares' not in respuestas:
                    return "¿Tienes latidos irregulares? (yes/no)"
                if respuestas.get('latidos_irregulares'):
                    return "Diagnóstico probable: Arritmia cardíaca."
                else:
                    return "Diagnóstico probable: Asma."
        else:  # dolor_pecho == False
            if 'fatiga' not in respuestas:
                return "¿Sientes fatiga? (yes/no)"
            fatiga = respuestas.get('fatiga')
            if fatiga:
                if 'hinchazon_extremidades' not in respuestas:
                    return "¿Tienes hinchazón en las extremidades? (yes/no)"
                if respuestas.get('hinchazon_extremidades'):
                    return "Diagnóstico probable: Insuficiencia cardíaca."
                else:
                    return "Diagnóstico probable: Fatiga con dificultad respiratoria - evaluar función cardíaca."

            else:
                if 'tos' not in respuestas:
                    return "¿Tienes tos? (yes/no)"
                tos = respuestas.get('tos')
                if tos:
                    if 'tos_seca' not in respuestas:
                        return "¿La tos es seca? (yes/no)"
                    tos_seca = respuestas.get('tos_seca')
                    if tos_seca:
                        return "Diagnóstico probable: Asma."
                    else:
                        if 'tos_flema' not in respuestas:
                            return "¿La tos tiene flema? (yes/no)"
                        tos_flema = respuestas.get('tos_flema')
                        if tos_flema:
                            if 'fiebre' not in respuestas:
                                return "¿Tienes fiebre? (yes/no)"
                            fiebre = respuestas.get('fiebre')
                            if fiebre:
                                return "Diagnóstico probable: Neumonía."
                            else:
                                return "Diagnóstico probable: Bronquitis."
                        else:
                            if 'tos_sangre' not in respuestas:
                                return "¿Toses sangre? (yes/no)"
                            tos_sangre = respuestas.get('tos_sangre')
                            if tos_sangre:
                                return "Diagnóstico probable: Tuberculosis."
                            else:
                                return "Diagnóstico probable: Bronquitis leve."
                else:
                    return "Diagnóstico probable: Dificultad respiratoria sin otros síntomas - evaluar función pulmonar."
    
    return "Diagnóstico probable: Requiere evaluación médica adicional."

def ruta_fiebre(respuestas):
    if 'fiebre' not in respuestas:
        return "¿Tienes fiebre? (yes/no)"
    
    if not respuestas.get('fiebre'):
        return "No se detecta fiebre. Evaluar otros síntomas."

    # Inicia análisis en base a fiebre presente
    if 'tos' not in respuestas:
        return "¿Tienes tos? (yes/no)"
    
    if respuestas.get('tos'):
        if 'tos_seca' not in respuestas:
            return "¿La tos es seca? (yes/no)"
        if respuestas.get('tos_seca'):
            if 'dificultad_respirar' not in respuestas:
                return "¿Tienes dificultad para respirar? (yes/no)"
            if respuestas.get('dificultad_respirar'):
                if 'dolor_pecho' not in respuestas:
                    return "¿Tienes dolor en el pecho? (yes/no)"
                if respuestas.get('dolor_pecho'):
                    if 'escalofrios' not in respuestas:
                        return "¿Tienes escalofríos? (yes/no)"
                    if respuestas.get('escalofrios'):
                        return "Diagnóstico probable: Neumonía"
                    else:
                        return "Diagnóstico probable: Bronquitis"
                else:
                    return "Diagnóstico probable: Asma con fiebre"
            else:
                return "Diagnóstico probable: Infección leve del tracto respiratorio"
        else:
            # tos con flema
            if 'tos_flema' not in respuestas:
                return "¿Tienes tos con flema? (yes/no)"
            if respuestas.get('tos_flema'):
                if 'flema_amarilla_verde' not in respuestas:
                    return "¿La flema es amarilla o verde? (yes/no)"
                if respuestas.get('flema_amarilla_verde'):
                    if 'fiebre_prolongada' not in respuestas:
                        return "¿Has tenido fiebre prolongada? (yes/no)"
                    if respuestas.get('fiebre_prolongada'):
                        return "Diagnóstico probable: Neumonía"
                    else:
                        return "Diagnóstico probable: Bronquitis"
                else:
                    return "Diagnóstico probable: Gripe o Influenza"
            else:
                if 'tos_sangre' not in respuestas:
                    return "¿Toses con sangre? (yes/no)"
                if respuestas.get('tos_sangre'):
                    if 'perdida_peso' not in respuestas:
                        return "¿Has perdido peso? (yes/no)"
                    if respuestas.get('perdida_peso'):
                        return "Diagnóstico probable: Tuberculosis"
                    else:
                        if 'escalofrios' not in respuestas:
                            return "¿Tienes escalofríos? (yes/no)"
                        if respuestas.get('escalofrios'):
                            return "Diagnóstico probable: Neumonía"
                        else:
                            if 'dolor_toser' not in respuestas:
                                return "¿Te duele al toser? (yes/no)"
                            if respuestas.get('dolor_toser'):
                                return "Diagnóstico probable: Infección pulmonar severa"
                            else:
                                return "Diagnóstico probable: Bronquitis"
                else:
                    return "Diagnóstico probable: Tos con fiebre - evaluar infección respiratoria"
    else:
        # No tiene tos
        if 'dolor_cabeza' not in respuestas:
            return "¿Tienes dolor de cabeza? (yes/no)"
        if respuestas.get('dolor_cabeza'):
            if 'nausea' not in respuestas:
                return "¿Tienes náuseas? (yes/no)"
            if respuestas.get('nausea'):
                if 'sensibilidad_luz' not in respuestas:
                    return "¿Tienes sensibilidad a la luz? (yes/no)"
                if respuestas.get('sensibilidad_luz'):
                    return "Diagnóstico probable: Migraña con fiebre"
                else:
                    if 'rigidez_cuello' not in respuestas:
                        return "¿Tienes rigidez en el cuello? (yes/no)"
                    if respuestas.get('rigidez_cuello'):
                        return "Diagnóstico probable: Meningitis"
                    else:
                        return "Diagnóstico probable: Gastroenteritis o cefalea"
            else:
                if 'brote_piel' not in respuestas:
                    return "¿Tienes brotes en la piel? (yes/no)"
                if respuestas.get('brote_piel'):
                    return "Diagnóstico probable: Dengue"
                else:
                    if 'convulsiones' not in respuestas:
                        return "¿Has tenido convulsiones? (yes/no)"
                    if respuestas.get('convulsiones'):
                        return "Diagnóstico probable: Meningitis"
                    else:
                        return "Diagnóstico probable: Fiebre con dolor de cabeza - evaluar infección viral"
        else:
            # No tiene dolor de cabeza
            if 'dolor_bajo_abdomen' not in respuestas:
                return "¿Tienes dolor en la parte baja del abdomen? (yes/no)"
            if respuestas.get('dolor_bajo_abdomen'):
                return "Diagnóstico probable: Infección urinaria"
            else:
                # No tiene dolor cabeza ni bajo abdomen
                if 'dolor_muscular' not in respuestas:
                    return "¿Tienes dolor muscular? (yes/no)"
                if respuestas.get('dolor_muscular'):
                    if 'brote_piel' not in respuestas:
                        return "¿Tienes brotes en la piel? (yes/no)"
                    if respuestas.get('brote_piel'):
                        if 'inflamacion' not in respuestas:
                            return "¿Hay inflamación? (yes/no)"
                        if respuestas.get('inflamacion'):
                            return "Diagnóstico probable: Dengue"
                        else:
                            return "Diagnóstico probable: Alergia con fiebre"
                    else:
                        return "Diagnóstico probable: Influenza"
                else:
                    if 'sudoracion_excesiva' not in respuestas:
                        return "¿Tienes sudoración excesiva? (yes/no)"
                    if respuestas.get('sudoracion_excesiva'):
                        if 'tos_persistente' not in respuestas:
                            return "¿Tienes tos persistente? (yes/no)"
                        if respuestas.get('tos_persistente'):
                            if 'tos_sangre' not in respuestas:
                                return "¿Toses con sangre? (yes/no)"
                            if respuestas.get('tos_sangre'):
                                return "Diagnóstico probable: Tuberculosis"
                            else:
                                return "Diagnóstico probable: Neumonía"
                        else:
                            if 'sudor_escalofrios' not in respuestas:
                                return "¿Tienes sudor con escalofríos? (yes/no)"
                            if respuestas.get('sudor_escalofrios'):
                                return "Diagnóstico probable: Neumonía"
                            else:
                                return "Diagnóstico probable: Fiebre con sudoración - evaluar infección"
                    else:
                        if 'fatiga' not in respuestas:
                            return "¿Tienes fatiga? (yes/no)"
                        if respuestas.get('fatiga'):
                            return "Diagnóstico probable: Síndrome febril - evaluar infección viral"
                        else:
                            return "Diagnóstico probable: Fiebre sin síntomas específicos - evaluar con médico"

    return "Diagnóstico probable: Fiebre - requiere evaluación médica adicional."

def ruta_dolor_pecho(respuestas):
    if 'dolor_pecho' not in respuestas:
        return "¿Tienes dolor en el pecho? (yes/no)"
    
    if not respuestas.get('dolor_pecho'):
        return "No se detecta dolor en el pecho. Evaluar otros síntomas."

    if 'mareo_debilidad' not in respuestas:
        return "¿Tienes mareo o debilidad? (yes/no)"

    if respuestas.get('mareo_debilidad'):
        if 'dolor_brazo_izquierdo' not in respuestas:
            return "¿Tienes dolor en el brazo izquierdo? (yes/no)"
        if respuestas.get('dolor_brazo_izquierdo'):
            return "Diagnóstico probable: Pre-infarto"
        else:
            if 'palpitaciones_irregulares' not in respuestas:
                return "¿Tienes palpitaciones irregulares? (yes/no)"
            if respuestas.get('palpitaciones_irregulares'):
                return "Diagnóstico probable: Arritmia cardíaca"
            else:
                if 'sudoracion_excesiva' not in respuestas:
                    return "¿Tienes sudoración excesiva? (yes/no)"
                if respuestas.get('sudoracion_excesiva'):
                    return "Diagnóstico probable: Ataque de pánico"
                else:
                    if 'temblores' not in respuestas:
                        return "¿Tienes temblores? (yes/no)"
                    if not respuestas.get('temblores'):
                        return "Diagnóstico probable: Hipertensión arterial"
                    else:
                        return "Diagnóstico probable: Ansiedad con dolor torácico"

    else:  # mareo_debilidad == False
        if 'nausea' not in respuestas:
            return "¿Tienes náuseas? (yes/no)"
        if respuestas.get('nausea'):
            if 'dolor_pecho_insoportable' not in respuestas:
                return "¿El dolor en el pecho es insoportable? (yes/no)"
            if respuestas.get('dolor_pecho_insoportable'):
                return "Diagnóstico probable: Pre-infarto"
            else:
                if 'reflujo' not in respuestas:
                    return "¿Tienes reflujo? (yes/no)"
                if respuestas.get('reflujo'):
                    return "Diagnóstico probable: Gastritis"
                else:
                    return "Diagnóstico probable: Dolor torácico con náuseas - evaluar gastritis o cardíaco"
        else:
            # Sin náuseas ni mareo
            if 'dificultad_respirar' not in respuestas:
                return "¿Tienes dificultad para respirar? (yes/no)"
            if respuestas.get('dificultad_respirar'):
                return "Diagnóstico probable: Posible problema cardíaco o pulmonar"
            else:
                if 'dolor_esfuerzo' not in respuestas:
                    return "¿El dolor empeora con el esfuerzo? (yes/no)"
                if respuestas.get('dolor_esfuerzo'):
                    return "Diagnóstico probable: Angina de pecho"
                else:
                    return "Diagnóstico probable: Dolor torácico atípico - evaluar con médico"

    return "Diagnóstico probable: Dolor en el pecho - requiere evaluación médica."

def ruta_dolor_abdominal(respuestas):
    if 'dolor_abdominal' not in respuestas:
        return "¿Tienes dolor abdominal? (yes/no)"
    
    if not respuestas.get('dolor_abdominal'):
        return "No se reporta dolor abdominal. Evaluar otros síntomas."

    # Con dolor abdominal
    if 'nausea' not in respuestas:
        return "¿Tienes náuseas? (yes/no)"

    if respuestas.get('nausea'):
        if 'acidez_ardor' not in respuestas:
            return "¿Sientes acidez o ardor en el estómago? (yes/no)"
        if respuestas.get('acidez_ardor'):
            return "Diagnóstico probable: Gastritis."
        else:
            if 'lado_derecho_abdomen' not in respuestas:
                return "¿El dolor está en el lado derecho del abdomen? (yes/no)"
            if respuestas.get('lado_derecho_abdomen'):
                return "Diagnóstico probable: Apendicitis."
            else:
                if 'fiebre_dolor_baja' not in respuestas:
                    return "¿Tienes fiebre o dolor leve? (yes/no)"
                if respuestas.get('fiebre_dolor_baja'):
                    return "Diagnóstico probable: Infección urinaria."
                else:
                    return "Diagnóstico probable: Dolor abdominal con náuseas - evaluar gastroenteritis."
    
    # Si NO hay náuseas
    else:
        if 'dolor_lumbar' not in respuestas:
            return "¿Sientes dolor en la zona lumbar (parte baja de la espalda)? (yes/no)"
        if respuestas.get('dolor_lumbar'):
            if 'dolor_insoportable' not in respuestas:
                return "¿El dolor es insoportable? (yes/no)"
            if respuestas.get('dolor_insoportable'):
                return "Diagnóstico probable: Cólicos renales."
            else:
                if 'fiebre_ardor' not in respuestas:
                    return "¿Tienes fiebre o sensación de ardor al orinar? (yes/no)"
                if respuestas.get('fiebre_ardor'):
                    return "Diagnóstico probable: Infección urinaria."
                else:
                    return "Diagnóstico probable: Dolor lumbar con componente abdominal."
        else:
            # Sin dolor lumbar, evaluar otros síntomas
            if 'fiebre' not in respuestas:
                return "¿Tienes fiebre? (yes/no)"
            if respuestas.get('fiebre'):
                return "Diagnóstico probable: Infección abdominal - evaluar con médico."
            else:
                return "Diagnóstico probable: Dolor abdominal inespecífico - requiere evaluación médica."

def ruta_mareo_debilidad(respuestas):
    if 'mareo_debilidad' not in respuestas:
        return "¿Sientes mareo o debilidad? (yes/no)"
    
    if not respuestas.get('mareo_debilidad'):
        return "No se reporta mareo ni debilidad. Evaluar otros síntomas."

    # Sí hay mareo o debilidad
    if 'dolor_pecho' not in respuestas:
        return "¿Tienes dolor en el pecho? (yes/no)"
    
    if respuestas.get('dolor_pecho'):
        if 'dolor_insoportable' not in respuestas:
            return "¿El dolor en el pecho es insoportable? (yes/no)"
        if respuestas.get('dolor_insoportable'):
            return "Diagnóstico probable: Pre-infarto."
        else:
            if 'palpitaciones_irregulares' not in respuestas:
                return "¿Tienes palpitaciones irregulares? (yes/no)"
            if respuestas.get('palpitaciones_irregulares'):
                return "Diagnóstico probable: Arritmia cardíaca."
            else:
                if 'sudoracion_excesiva' not in respuestas:
                    return "¿Tienes sudoración excesiva? (yes/no)"
                if respuestas.get('sudoracion_excesiva'):
                    return "Diagnóstico probable: Ataque de pánico."
                else:
                    if 'temblores' not in respuestas:
                        return "¿Tienes temblores? (yes/no)"
                    if not respuestas.get('temblores'):
                        return "Diagnóstico probable: Hipertensión arterial."
                    else:
                        return "Diagnóstico probable: Ansiedad con síntomas cardíacos."
    
    else:  # dolor_pecho == False
        if 'perdida_conciencia' not in respuestas:
            return "¿Has perdido el conocimiento? (yes/no)"
        if respuestas.get('perdida_conciencia'):
            if 'fue_repentino' not in respuestas:
                return "¿La pérdida de conciencia fue repentina? (yes/no)"
            if respuestas.get('fue_repentino'):
                return "Diagnóstico probable: Arritmia cardíaca."
            else:
                if 'antes_dolor_pecho' not in respuestas:
                    return "¿Sentiste dolor en el pecho antes del desmayo? (yes/no)"
                if respuestas.get('antes_dolor_pecho'):
                    return "Diagnóstico probable: Pre-infarto."
                else:
                    if 'estres' not in respuestas:
                        return "¿Has estado bajo mucho estrés últimamente? (yes/no)"
                    if respuestas.get('estres'):
                        return "Diagnóstico probable: Ataque de pánico."
                    else:
                        return "Diagnóstico probable: Síncope - evaluar causas."
        else:  # No hubo pérdida de conciencia
            if 'sudoracion_excesiva' not in respuestas:
                return "¿Tienes sudoración excesiva? (yes/no)"
            if respuestas.get('sudoracion_excesiva'):
                if 'temblores_hambre' not in respuestas:
                    return "¿Tienes temblores o sensación de hambre? (yes/no)"
                if respuestas.get('temblores_hambre'):
                    return "Diagnóstico probable: Bajón de azúcar."
                else:
                    return "Diagnóstico probable: Sudoración con mareo - evaluar causas metabólicas."
            else:
                if 'fatiga' not in respuestas:
                    return "¿Tienes fatiga? (yes/no)"
                if respuestas.get('fatiga'):
                    return "Diagnóstico probable: Fatiga con mareo - evaluar anemia o problemas metabólicos."
                else:
                    return "Diagnóstico probable: Mareo inespecífico - evaluar presión arterial."

def ruta_nausea_vomito(respuestas):
    if 'nausea_vomito' not in respuestas:
        return "¿Tienes náuseas o vómito? (yes/no)"
    
    if not respuestas.get('nausea_vomito'):
        return "No se reporta náuseas ni vómito. Evaluar otros síntomas."

    if 'dolor_abdominal' not in respuestas:
        return "¿Tienes dolor abdominal? (yes/no)"
    
    if respuestas.get('dolor_abdominal'):
        if 'dolor_abdominal_insoportable' not in respuestas:
            return "¿El dolor abdominal es insoportable? (yes/no)"
        if respuestas.get('dolor_abdominal_insoportable'):
            return "Diagnóstico probable: Apendicitis."
        else:
            if 'acidez_ardor' not in respuestas:
                return "¿Sientes acidez o ardor estomacal? (yes/no)"
            if respuestas.get('acidez_ardor'):
                return "Diagnóstico probable: Gastritis."
            else:
                if 'orina_sangre' not in respuestas:
                    return "¿Hay sangre en la orina? (yes/no)"
                if respuestas.get('orina_sangre'):
                    if 'parte_baja_espalda' not in respuestas:
                        return "¿Tienes dolor en la parte baja de la espalda? (yes/no)"
                    if respuestas.get('parte_baja_espalda'):
                        return "Diagnóstico probable: Cólico renal."
                    else:
                        return "Diagnóstico probable: Infección urinaria con hematuria."
                else:
                    return "Diagnóstico probable: Gastroenteritis."
    
    else:  # dolor_abdominal == False
        if 'dolor_cabeza' not in respuestas:
            return "¿Tienes dolor de cabeza? (yes/no)"
        if respuestas.get('dolor_cabeza'):
            if 'sensibilidad_luz_ruido' not in respuestas:
                return "¿Tienes sensibilidad a la luz o al ruido? (yes/no)"
            if respuestas.get('sensibilidad_luz_ruido'):
                return "Diagnóstico probable: Migraña."
            else:
                if 'fiebre_rigidez_cuello' not in respuestas:
                    return "¿Tienes fiebre y rigidez en el cuello? (yes/no)"
                if respuestas.get('fiebre_rigidez_cuello'):
                    return "Diagnóstico probable: Meningitis."
                else:
                    if 'golpe_cabeza' not in respuestas:
                        return "¿Recibiste un golpe en la cabeza recientemente? (yes/no)"
                    if respuestas.get('golpe_cabeza'):
                        return "Diagnóstico probable: Conmoción cerebral / vigilancia 24h."
                    else:
                        if 'vision_borrosa' not in respuestas:
                            return "¿Tienes visión borrosa? (yes/no)"
                        if respuestas.get('vision_borrosa'):
                            if 'dificultad_hablar' not in respuestas:
                                return "¿Tienes dificultad para hablar? (yes/no)"
                            if respuestas.get('dificultad_hablar'):
                                return "Diagnóstico probable: Accidente cerebrovascular."
                            else:
                                return "Diagnóstico probable: Hipertensión arterial."
                        else:
                            return "Diagnóstico probable: Cefalea con náuseas."
        else:
            # Sin dolor de cabeza
            if 'mareo_debilidad' not in respuestas:
                return "¿Tienes mareo o debilidad? (yes/no)"
            if respuestas.get('mareo_debilidad'):
                if 'sudoracion_temblores' not in respuestas:
                    return "¿Tienes sudoración o temblores? (yes/no)"
                if respuestas.get('sudoracion_temblores'):
                    return "Diagnóstico probable: Bajón de azúcar."
                else:
                    if 'sol_calor' not in respuestas:
                        return "¿Has estado expuesto al sol o calor excesivo? (yes/no)"
                    if respuestas.get('sol_calor'):
                        return "Diagnóstico probable: Golpe de calor."
                    else:
                        if 'sustancia_toxica' not in respuestas:
                            return "¿Consumiste alguna sustancia tóxica recientemente? (yes/no)"
                        if respuestas.get('sustancia_toxica'):
                            return "Diagnóstico probable: Intoxicación."
                        else:
                            return "Diagnóstico probable: Náuseas con mareo - evaluar causas gastrointestinales."
            else:
                return "Diagnóstico probable: Náuseas aisladas - evaluar gastritis o infección viral."

def ruta_perdida_conciencia(respuestas):
    if 'perdida_conciencia' not in respuestas:
        return "¿Has perdido la conciencia recientemente? (yes/no)"
    
    if not respuestas.get('perdida_conciencia'):
        return "No se reporta pérdida de conciencia. Evaluar otros síntomas."

    if 'mareo_debilidad' not in respuestas:
        return "¿Tuviste mareo o debilidad antes de perder la conciencia? (yes/no)"
    
    if respuestas.get('mareo_debilidad'):
        if 'latidos_irregulares' not in respuestas:
            return "¿Sentiste latidos irregulares del corazón antes del evento? (yes/no)"
        if respuestas.get('latidos_irregulares'):
            return "Diagnóstico probable: Arritmia cardíaca."
        else:
            if 'dolor_pecho_antes' not in respuestas:
                return "¿Tuviste dolor en el pecho antes del desmayo? (yes/no)"
            if respuestas.get('dolor_pecho_antes'):
                if 'dolor_pecho_repite' not in respuestas:
                    return "¿El dolor en el pecho ha sido recurrente? (yes/no)"
                if respuestas.get('dolor_pecho_repite'):
                    return "Diagnóstico probable: Infarto miocárdico."
                else:
                    return "Diagnóstico probable: Insuficiencia cardíaca."
            else:
                if 'sudor_ansiedad_antes' not in respuestas:
                    return "¿Sentiste sudor o ansiedad antes de perder la conciencia? (yes/no)"
                if respuestas.get('sudor_ansiedad_antes'):
                    return "Diagnóstico probable: Ataque de pánico."
                else:
                    if 'sudor_vision_confusion' not in respuestas:
                        return "¿Experimentaste sudoración, visión borrosa o confusión antes? (yes/no)"
                    if respuestas.get('sudor_vision_confusion'):
                        return "Diagnóstico probable: Accidente cerebrovascular."
                    else:
                        if 'temblores_hambre' not in respuestas:
                            return "¿Tuviste temblores o sensación de hambre antes? (yes/no)"
                        if respuestas.get('temblores_hambre'):
                            return "Diagnóstico probable: Bajón de azúcar."
                        else:
                            return "Diagnóstico probable: Síncope vasovagal."
    else:
        # Sin mareo previo
        if 'fue_repentino' not in respuestas:
            return "¿La pérdida de conciencia fue repentina? (yes/no)"
        if respuestas.get('fue_repentino'):
            if 'convulsiones' not in respuestas:
                return "¿Tuviste convulsiones? (yes/no)"
            if respuestas.get('convulsiones'):
                return "Diagnóstico probable: Epilepsia o crisis convulsiva."
            else:
                return "Diagnóstico probable: Arritmia cardíaca súbita."
        else:
            if 'sustancia_exceso' not in respuestas:
                return "¿Consumiste alguna sustancia en exceso? (yes/no)"
            if respuestas.get('sustancia_exceso'):
                return "Diagnóstico probable: Intoxicación."
            else:
                return "Diagnóstico probable: Síncope de causa desconocida - requiere evaluación médica."

def ruta_brote_piel(respuestas):
    if 'brote_piel' not in respuestas:
        return "¿Tienes un brote en la piel? (yes/no)"
    
    if not respuestas.get('brote_piel'):
        return "No se reporta brote en la piel. Evaluar otros síntomas."

    if 'dolor_muscular' not in respuestas:
        return "¿Tienes dolor muscular? (yes/no)"
    
    if respuestas.get('dolor_muscular'):
        if 'fiebre_reciente' not in respuestas:
            return "¿Has tenido fiebre recientemente? (yes/no)"
        if respuestas.get('fiebre_reciente'):
            return "Diagnóstico probable: Dengue."
        else:
            if 'alergico_sustancia' not in respuestas:
                return "¿Eres alérgico a alguna sustancia? (yes/no)"
            if respuestas.get('alergico_sustancia'):
                if 'tocado_sustancia' not in respuestas:
                    return "¿Has estado en contacto con la sustancia alérgica? (yes/no)"
                if respuestas.get('tocado_sustancia'):
                    return "Diagnóstico probable: Alergia."
                else:
                    return "Diagnóstico probable: Brote cutáneo con dolor muscular - evaluar causas."
            else:
                if 'inflamacion' not in respuestas:
                    return "¿Tienes inflamación en el área afectada? (yes/no)"
                if respuestas.get('inflamacion'):
                    return "Diagnóstico probable: Dermatitis inflamatoria."
                else:
                    return "Diagnóstico probable: Brote cutáneo con dolor muscular - evaluar infección viral."

    else:
        # Sin dolor muscular
        if 'nausea' not in respuestas:
            return "¿Tienes náuseas? (yes/no)"
        if respuestas.get('nausea'):
            if 'fiebre_reciente' not in respuestas:
                return "¿Has tenido fiebre recientemente? (yes/no)"
            if respuestas.get('fiebre_reciente'):
                return "Diagnóstico probable: Dengue."
            else:
                if 'alergico_sustancia' not in respuestas:
                    return "¿Eres alérgico a alguna sustancia? (yes/no)"
                if respuestas.get('alergico_sustancia'):
                    if 'tocado_sustancia' not in respuestas:
                        return "¿Has estado en contacto con la sustancia alérgica? (yes/no)"
                    if respuestas.get('tocado_sustancia'):
                        return "Diagnóstico probable: Alergia."
                    else:
                        return "Diagnóstico probable: Brote cutáneo con náuseas - evaluar reacción alérgica."
                else:
                    return "Diagnóstico probable: Brote cutáneo con náuseas - evaluar infección viral."
        else:
            # Sin náuseas
            if 'alergico_sustancia' not in respuestas:
                return "¿Eres alérgico a alguna sustancia? (yes/no)"
            if respuestas.get('alergico_sustancia'):
                if 'tocado_sustancia' not in respuestas:
                    return "¿Has estado en contacto con la sustancia alérgica? (yes/no)"
                if respuestas.get('tocado_sustancia'):
                    return "Diagnóstico probable: Alergia."
                else:
                    return "Diagnóstico probable: Brote cutáneo - evaluar otras causas."
            else:
                if 'inflamacion' not in respuestas:
                    return "¿Tienes inflamación en el área afectada? (yes/no)"
                if respuestas.get('inflamacion'):
                    return "Diagnóstico probable: Dermatitis."
                else:
                    return "Diagnóstico probable: Brote cutáneo inespecífico - evaluar con dermatólogo."

def ruta_accidente_golpe(respuestas):
    if 'accidente_golpe' not in respuestas:
        return "¿Has tenido un accidente o golpe? (yes/no)"
    
    if not respuestas.get('accidente_golpe'):
        return "No hay reporte de accidente o golpe. Evaluar otros síntomas."

    # ¿Herida abierta?
    if 'herida_abierta' not in respuestas:
        return "¿Tienes herida abierta? (yes/no)"
    
    if respuestas.get('herida_abierta'):
        if 'sangrado_profundo' not in respuestas:
            return "¿El sangrado es profundo? (yes/no)"
        if respuestas.get('sangrado_profundo'):
            if 'signos_infeccion' not in respuestas:
                return "¿Presentas signos de infección en la herida? (yes/no)"
            if respuestas.get('signos_infeccion'):
                return "Diagnóstico probable: Herida infectada."
            else:
                # No hay infección, pero hay sangrado profundo
                if 'hinchazon_forma_anormal' not in respuestas:
                    return "¿Hay hinchazón o forma anormal en la zona afectada? (yes/no)"
                if respuestas.get('hinchazon_forma_anormal'):
                    if 'estructura_osea_expuesta' not in respuestas:
                        return "¿Hay estructura ósea expuesta? (yes/no)"
                    if respuestas.get('estructura_osea_expuesta'):
                        return "Diagnóstico probable: Fractura abierta."
                    else:
                        return "Diagnóstico probable: Dislocación con herida abierta."
                else:
                    return "Diagnóstico probable: Herida profunda sin complicaciones."
        else:
            # Herida abierta pero no profunda
            if 'signos_infeccion' not in respuestas:
                return "¿Presentas signos de infección en la herida? (yes/no)"
            if respuestas.get('signos_infeccion'):
                return "Diagnóstico probable: Herida infectada."
            else:
                return "Diagnóstico probable: Herida superficial - limpiar y curar."

    # Herida NO abierta
    else:
        if 'hinchazon_forma_anormal' not in respuestas:
            return "¿Hay hinchazón o forma anormal en la zona afectada? (yes/no)"
        if respuestas.get('hinchazon_forma_anormal'):
            # Hay hinchazón y forma anormal
            if 'puede_mover_extremidad' not in respuestas:
                return "¿Puedes mover la extremidad afectada? (yes/no)"
            if respuestas.get('puede_mover_extremidad'):
                return "Diagnóstico probable: Dislocación sin herida abierta."
            else:
                return "Diagnóstico probable: Fractura cerrada."
        else:
            # No hay hinchazón anormal
            if 'dolor_intenso' not in respuestas:
                return "¿Tienes dolor intenso en la zona? (yes/no)"
            if respuestas.get('dolor_intenso'):
                return "Diagnóstico probable: Contusión severa."
            else:
                return "Diagnóstico probable: Contusión leve - aplicar hielo y reposo."