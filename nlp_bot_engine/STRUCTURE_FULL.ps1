# ===== ANVÄNDARINSTÄLLNINGAR =====
# Ändra dessa värden efter behov

# Inställningar för visning
$showFiles = $true         # Sätt till $true för att visa filer, $false för att bara visa mappar
$maxDepth = 5               # Hur många nivåer djupt skriptet ska gå i undermapparna
$outputFile = "./STRUCTURE_map.md"  # Relativ sökväg för utfilen

# Mappar att ignorera (lägg till eller ta bort enligt behov)
$excludeDirs = @(
    "venv", "env", "__pycache__", "node_modules", ".git", "_unimplemented_Developmemt",
    "bin", "obj", "build", "dist", "coverage", "logs", "NodeX.egg-info",
    ".next", ".nuxt", ".output", ".cache",
    "target", "out", ".idea", ".vscode", "pdf", "Scripts", "COPIAX_LORA", 
    "extracted_data", "converted_docs", "Compatibility_Trainingdata", "compatibility",
    "backup", "artikel", "a", "pattern_analysis_results", "technical", "Dataintegreringsmodul", "Frameworks_python_claude",
    "Docs_Original", "Docs", "Backup", "_"
)

# Filer att ignorera när $showFiles = $true
$excludeFiles = @(
    ".DS_Store", "*.pyc", "*.pyo", "*.pyd",
    ".env.local", ".env.*.local",
    "npm-debug.log*", "yarn-debug.log*", "yarn-error.log*",
    "*.log", "*.swp", "*.swo",
    ".eslintcache", ".tsbuildinfo"
)

# ===== SKRIPTLOGIK - ÄNDRA INTE NEDAN DENNA LINJE =====

# Hämta nuvarande mappens sökväg
$currentPath = Get-Location

# Funktion för att hämta ikon baserat på filändelse
function Get-FileIcon {
    param (
        [string]$Extension
    )
    
    $icons = @{
        # Webb-utveckling
        '.html'     = '🌐'
        '.htm'      = '🌐'
        '.css'      = '🎨'
        '.scss'     = '🎨'
        '.sass'     = '🎨'
        '.less'     = '🎨'
        '.js'       = '📜'
        '.jsx'      = '⚛️'
        '.ts'       = '📘'
        '.tsx'      = '⚛️'
        '.vue'      = '💚'
        '.svelte'   = '🔥'

        # Backend & Programmering
        '.py'       = '🐍'
        '.java'     = '☕'
        '.class'    = '☕'
        '.rb'       = '💎'
        '.php'      = '🐘'
        '.cs'       = '#️⃣'
        '.cpp'      = '⚙️'
        '.c'        = '⚙️'
        '.go'       = '🐹'
        '.rs'       = '🦀'
        '.swift'    = '🕊️'
        '.kt'       = '📱'

        # Data & Konfiguration
        '.json'     = '📋'
        '.yaml'     = '⚙️'
        '.yml'      = '⚙️'
        '.xml'      = '📰'
        '.csv'      = '📊'
        '.sql'      = '🗄️'
        '.db'       = '🗄️'
        '.env'      = '🔒'
        '.toml'     = '⚙️'
        '.ini'      = '⚙️'
        '.config'   = '⚙️'
        '.lock'     = '🔒'

        # Dokumentation
        '.md'       = '📝'
        '.mdx'      = '📝'
        '.txt'      = '📄'
        '.pdf'      = '📕'
        '.doc'      = '📘'
        '.docx'     = '📘'
        '.xls'      = '📗'
        '.xlsx'     = '📗'

        # Bilder & Media
        '.jpg'      = '🖼️'
        '.jpeg'     = '🖼️'
        '.png'      = '🖼️'
        '.gif'      = '🖼️'
        '.svg'      = '🎨'
        '.ico'      = '🖼️'
        '.mp4'      = '🎥'
        '.mp3'      = '🎵'
        '.wav'      = '🎵'

        # Utvecklingsverktyg
        '.git'      = '📦'
        '.gitignore' = '👁️'
        '.dockerignore' = '🐳'
        '.dockerfile' = '🐳'
        '.eslintrc'  = '🔍'
        '.prettierrc' = '✨'
        '.babelrc'   = '🔧'
        '.npmrc'     = '📦'
        '.nvmrc'     = '📦'
    }

    $ext = [System.IO.Path]::GetExtension($Extension).ToLower()
    if ($icons.ContainsKey($ext)) {
        return $icons[$ext]
    }
    return '📄'
}

# Huvudfunktion för att generera mappstrukturen
function Get-DirectoryTree {
    param (
        [string]$Path = $currentPath,
        [int]$IndentLevel = 0,
        [int]$MaxDepth = $maxDepth,
        [bool]$ShowFiles = $showFiles,
        [string[]]$ExcludeDirs = $excludeDirs,
        [string[]]$ExcludeFiles = $excludeFiles
    )

    # Visa rotmappen när vi börjar
    if ($IndentLevel -eq 0) {
        Write-Output "`n📁 $(Split-Path $Path -Leaf)"
    }

    # Avsluta om vi nått maxdjupet
    if ($IndentLevel -ge $MaxDepth) {
        return
    }

    # Hämta objekt, antingen bara mappar eller alla objekt beroende på inställning
    $items = if (-not $ShowFiles) {
        Get-ChildItem -Path $Path -Directory
    } else {
        Get-ChildItem -Path $Path
    }

    foreach ($item in $items) {
        $shouldSkip = $false
        
        if ($item.PSIsContainer) {
            # Kontrollera om mappen finns i exkluderingslistan
            if ($ExcludeDirs -contains $item.Name) {
                $shouldSkip = $true
            } else {
                # Kontrollera om mappen är en kopia av en ignorerad mapp
                foreach ($excludeDir in $ExcludeDirs) {
                    if ($item.Name -match "^$excludeDir\s+(copy|kopior)(\s+\d+)?$") {
                        $shouldSkip = $true
                        break
                    }
                }
            }
        } else {
            # Kontrollera om filen ska ignoreras
            foreach ($pattern in $ExcludeFiles) {
                if ($item.Name -like $pattern) {
                    $shouldSkip = $true
                    break
                }
            }
        }

        if ($shouldSkip) { continue }

        $indent = "    " * $IndentLevel

        if ($item.PSIsContainer) {
            # Detta är en mapp
            Write-Output "$indent├── 📁 $($item.Name)"
            
            # Rekursivt anrop för undermappar
            Get-DirectoryTree -Path $item.FullName -IndentLevel ($IndentLevel + 1) -MaxDepth $MaxDepth -ShowFiles $ShowFiles -ExcludeDirs $ExcludeDirs -ExcludeFiles $ExcludeFiles
        } elseif ($ShowFiles) {
            # Detta är en fil och vi vill visa filer
            $icon = Get-FileIcon -Extension $item.Name
            Write-Output "$indent├── $icon $($item.Name)"
        }
    }
}

# Kör och visa information om vad som genereras
Write-Host "Genererar mappstruktur..." -ForegroundColor Cyan
if ($showFiles) {
    Write-Host "Visar både mappar och filer till djupet $maxDepth" -ForegroundColor Cyan
} else {
    Write-Host "Visar endast mappar till djupet $maxDepth" -ForegroundColor Cyan
}

# Kör funktionen och fånga resultatet
$result = Get-DirectoryTree

# Visa resultatet i terminalen
$result | ForEach-Object { Write-Host $_ }

# Spara resultatet till fil
$result | Out-File -FilePath $outputFile -Encoding utf8

Write-Host "`nMappstrukturen har sparats till $outputFile" -ForegroundColor Green