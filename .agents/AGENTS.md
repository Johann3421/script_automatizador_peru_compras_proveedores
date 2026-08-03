# AGENTS.md - Workspace Rules & Configurations

## Active Modes (Ultra)
- **Caveman (ultra):** Extreme token saving. Zero fluff. Direct code/commands + essential keywords. Drop non-essential grammar (articles, pronouns, filler). 100% technical accuracy.
- **Ponytail (ultra):** YAGNI extremist. Prefer stdlib/native over dependencies. Deletion over addition. Minimal diffs. Challenge over-engineering immediately.

## Commands Reference
- `/caveman [lite|full|ultra]` - Toggle Caveman verbosity level.
- `/ponytail [lite|full|ultra]` - Toggle Ponytail intensity level.
- `/ponytail-audit` - Scan whole repo for bloat/over-engineering.
- `/ponytail-review` - Review diff for over-engineering.
- `/ponytail-debt` - Track `ponytail:` comments in codebase.
- `/ponytail-gain` - Show savings scoreboard.
- `/ponytail-help` - Ponytail quick reference.

## Project Structure & Key Directories
- **Workspace Root:** `d:\SISTEMAS 02\Desktop\Proyectos_generales\script_automatizador_peru_compras_proveedores`
- **Main Script:** [main.py](file:///d:/SISTEMAS%2002/Desktop/Proyectos_generales/script_automatizador_peru_compras_proveedores/main.py)
- **Automation Logic:** `automation/`
- **UI System:** `ui/`
- **Sub-modules:** `modulo_modificar_productos/`, `modulo_subir_pdf/`
- **Scripts & Tools:** `scripts/`, `extract_catalog.py`, `intercept_payload.py`
- **Utilities:** `utils/`, `resource_helper.py`
- **Packaging/Build:** `build_exe.py`, `build_installer.py`, `PeruComprasBot.spec`, `build/`, `dist/`, `installer/`
- **Agent Configs & Skills:** `.agents/`, `.agents/skills/`

# Reglas Base de Diseño y Desarrollo (Anti-IA & Ley de Tesler)

Antes de diseñar o programar cualquier parte de este sistema, sigue siempre estas reglas base, sin excepción:

1. **Ley de Tesler:** Toda la complejidad va en el backend (validaciones, cálculos, reglas de negocio, orquestación de datos). El frontend debe ser lo más simple posible, con pocos pasos y decisiones visibles, de modo que hasta un niño o una persona sin conocimientos técnicos pueda usarlo sin explicación previa. Nunca traslades al usuario una decisión que el sistema puede resolver solo.
2. **Evita que el diseño "huela" a IA:** No uses paletas genéricas de gradientes morado-azul, glassmorphism excesivo, sombras neón ni emojis como iconografía principal. Usa paletas simples de 2-3 colores neutros, buen contraste y tipografía sobria y coherente con el rubro del sistema.
3. **Imita patrones reales del rubro:** No repitas siempre el mismo layout ni patrones por defecto solo porque son los más fáciles de generar. Busca referencias reales de sistemas del mismo rubro hechos por personas o empresas en producción e imita esos patrones reales de uso en vez de estructuras automáticas típicas.
4. **Prioriza simplicidad funcional:** Menos pantallas, menos clics, menos campos. Si algo se puede inferir o automatizar, no se le pregunta al usuario. Usa mensajes de error y ayuda en lenguaje humano, no técnico. Flujos lineales y predecibles.
5. **Mantén el backend limpio y mantenible:** Separa lógica de negocio, acceso a datos y presentación; usa nomenclatura clara y consistente en todo el proyecto; nunca pongas lógica de negocio en el frontend.
6. **Verificación final antes de dar por terminada cualquier pantalla o funcionalidad:**
   - ¿Un usuario nuevo entendería qué hacer sin instrucciones?
   - ¿El diseño se ve simple y no genérico de IA?
   - ¿Se buscaron referencias reales antes de diseñar?
   - ¿Toda la complejidad quedó en el backend?
   - ¿El frontend tiene solo lo mínimo indispensable?
