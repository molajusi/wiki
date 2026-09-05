# 지식 누적 위키 AGY 실행 스크립트 (PowerShell)
$OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = "Stop"

try {
    Set-Location -Path "Z:\wiki"
    Write-Host "========================================================" -ForegroundColor Cyan
    Write-Host "  지식 누적 위키 AGY 실행기 (작업 디렉토리: Z:\wiki)" -ForegroundColor Cyan
    Write-Host "========================================================" -ForegroundColor Cyan
    Write-Host ""
    
    agy @args
} catch {
    Write-Host "[오류] Z:\wiki 디렉토리에 접근할 수 없습니다: $_" -ForegroundColor Red
    exit 1
}
