# Import naredba u Python projektima

Objašnjenje na primjerima iz Guitar Shop projekta kako funkcionira `import`.

## 1. Osnovni tipovi importa

### Apsolutni import (preporučeno)
Kreće od root direktorija projekta:

```python
# U app.py
from Core.guitars.guitars import Guitar
from Core.guitars.guitar_types import ElectricGuitar, AcousticGuitar
from Core.amps.amplifiers import Amplifier
from services.guitar_services.guitar_services import GuitarService
```

### Relativni import
Koristi se unutar paketa, relativno u odnosu na trenutnu lokaciju:

```python
# U Core/guitars/guitars.py
from ..commons.base_model import BaseModel  # Idemo 2 nivoa gore pa u commons
from .guitar_types import ElectricGuitar    # Iz istog direktorija
from ..amps.amp_types import TubeAmp        # Iz susjednog paketa
```

## 2. Praktični primjeri iz Guitar Shop projekta

### Primjer 1: U `Core/guitars/guitars.py`
```python
# Relativni import iz commons (nadređeni direktorij)
from ..commons.base_model import BaseModel

# Relativni import iz istog direktorija
from .guitar_types import ElectricGuitar, AcousticGuitar

# Apsolutni import iz accessories
from Core.accessories.strings import GuitarString

class Guitar(BaseModel):
    def __init__(self, name, strings):
        self.name = name
        self.strings = strings
```

### Primjer 2: U `services/guitar_services/guitar_services.py`
```python
# Apsolutni import iz Core modula
from Core.guitars.guitars import Guitar
from Core.guitars.guitar_types import ElectricGuitar
from Core.amps.amplifiers import Amplifier
from infrastructure.guitar_repos.guitar_db_repo import GuitarDbRepo

class GuitarService:
    def __init__(self):
        self.repo = GuitarDbRepo()
    
    def create_guitar(self, guitar_type, name):
        if guitar_type == "electric":
            return ElectricGuitar(name)
```

### Primjer 3: U `app.py` (root level)
```python
# Sve su apsolutni importi jer smo na root levelu
from Core.guitars.guitars import Guitar
from Core.guitars.guitar_types import ElectricGuitar, AcousticGuitar
from Core.amps.amplifiers import Amplifier
from Core.accessories.strings import GuitarString
from services.guitar_services.guitar_services import GuitarService
from infrastructure.guitar_repos.guitar_file_repo import GuitarFileRepo

# Korištenje
service = GuitarService()
guitar = ElectricGuitar("Fender Stratocaster")
```

## 3. __init__.py uloga

`__init__.py` fajlovi čine direktorije Python paketima. Možeš ih koristiti za pojednostavljivanje importa:

### U `Core/guitars/__init__.py`:
```python
from .guitars import Guitar
from .guitar_types import ElectricGuitar, AcousticGuitar

# Sada umjesto:
# from Core.guitars.guitars import Guitar

# Možeš:
# from Core.guitars import Guitar
```

### U `Core/__init__.py`:
```python
from .guitars import Guitar, ElectricGuitar, AcousticGuitar
from .amps import Amplifier
from .accessories import GuitarString

# Sada u app.py možeš:
# from Core import Guitar, ElectricGuitar, Amplifier
```

## 4. Oznake u importima

```python
# Točka (.) = trenutni direktorij
from .guitars import Guitar

# Dvije točke (..) = nadređeni direktorij
from ..commons import BaseModel

# Tri točke (...) = dva nivoa gore
from ...utils import helper
```

## 5. Česte greške

```python
# ❌ LOŠE - nećeš moći importati iz nadređenih direktorija
import guitars  # ako si u services/guitar_services

# ✅ DOBRO
from Core.guitars import guitars

# ❌ LOŠE - circular import
# guitar.py importa amplifier.py
# amplifier.py importa guitar.py

# ✅ DOBRO - koristi import unutar funkcije ako je nužan
def get_compatible_amps():
    from Core.amps.amplifiers import Amplifier
    return Amplifier.query_compatible()
```

## 6. Kompletan primjer - cijela struktura

### app.py
```python
from Core.guitars import Guitar, ElectricGuitar
from services.guitar_services import GuitarService

service = GuitarService()
guitar = service.create_guitar("electric", "Stratocaster")
```

### Core/guitars/guitars.py
```python
from ..commons.base_model import BaseModel
from ..accessories.strings import GuitarString

class Guitar(BaseModel):
    def __init__(self, name, strings):
        super().__init__()
        self.name = name
        self.strings = strings
```

### services/guitar_services/guitar_services.py
```python
from Core.guitars.guitars import Guitar
from Core.guitars.guitar_types import ElectricGuitar
from infrastructure.guitar_repos.guitar_db_repo import GuitarDbRepo

class GuitarService:
    def __init__(self):
        self.repo = GuitarDbRepo()
    
    def create_guitar(self, guitar_type, name):
        if guitar_type == "electric":
            return ElectricGuitar(name)
        return Guitar(name)
```

### infrastructure/guitar_repos/guitar_db_repo.py
```python
from Core.guitars.guitars import Guitar

class GuitarDbRepo:
    def save(self, guitar):
        # Logika za spremanje u bazu
        pass
```

## 7. Struktura projekta i pravila

```bash
C:.
├── app.py                          # Koristi apsolutne importe
├── Core/
│   ├── __init__.py                 # Eksportira glavne klase
│   ├── guitars/
│   │   ├── __init__.py
│   │   ├── guitars.py              # Koristi relativne importe unutar Core
│   │   └── guitar_types.py
│   ├── amps/
│   └── accessories/
├── services/
│   └── guitar_services/
│       ├── __init__.py
│       └── guitar_services.py      # Koristi apsolutne importe
└── infrastructure/
    └── guitar_repos/
        ├── __init__.py
        └── guitar_db_repo.py       # Koristi apsolutne importe
```

## 8. Best practices za tvoj projekt

1. **U app.py i services**: Koristi **apsolutne importe**
   ```python
   from Core.guitars.guitars import Guitar
   ```

2. **Unutar Core paketa**: Koristi **relativne importe**
   ```python
   from ..commons.base_model import BaseModel
   from .guitar_types import ElectricGuitar
   ```

3. **U infrastructure**: Koristi **apsolutne importe**
   ```python
   from Core.guitars.guitars import Guitar
   ```

4. **Populiraj __init__.py** fajlove za lakše importanje:
   ```python
   # Core/__init__.py
   from .guitars.guitars import Guitar
   from .guitars.guitar_types import ElectricGuitar, AcousticGuitar
   ```

## Zaključak

- **Apsolutni import**: `from Core.guitars.guitars import Guitar` - koristi za importanje između različitih paketa
- **Relativni import**: `from ..commons import BaseModel` - koristi unutar istog paketa (Core)
- **__init__.py**: Pojednostavljuje importe i pravi direktorije paketima
- **Pravilo**: Što je jasniji put, bolje! Izbegavaj komplikovane relativne importe gdje možeš.

🎸 Tvoja struktura je odlična za apsolutne importe iz app.py!