package main

import (
	"fmt"
	"os"
	"os/exec"
	"time"
)

func main() {
	// Comando Docker a ser executado
	currentDir, err := os.Getwd()
	if err != nil {
        fmt.Println("Erro ao obter o diretório atual:", err)
        return
    }
    volumePath := fmt.Sprintf("%s/resultados:/resultados", currentDir)

	fmt.Println("Caminho do volume:", volumePath)

	cmd := exec.Command("docker", "run", "-v", volumePath, "meu-container-python")

	// Iniciar o comando em segundo plano
	//err := cmd.Start()
	fmt.Println("Comando Docker a ser executado:", cmd.String())
	if err != nil {
		fmt.Println("Erro ao iniciar o comando Docker:", err)
		return
	}

	fmt.Println("Comando Docker em execução.")

	// Aguarde um tempo para permitir que o Docker execute
	time.Sleep(10 * time.Second)

	// Encerre o comando
	err = cmd.Process.Kill()
	if err != nil {
		fmt.Println("Erro ao encerrar o comando Docker:", err)
		return
	}

	fmt.Println("Comando Docker encerrado.")
}
