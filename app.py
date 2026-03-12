<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Presupuestador LAMBE EDICIONES</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 min-h-screen p-4 md:p-8">
    <div class="max-w-4xl mx-auto bg-white rounded-xl shadow-lg overflow-hidden">
        <div class="bg-blue-900 text-white p-6">
            <h1 class="text-2xl font-bold">Calculadora de Presupuestos - LAMBE</h1>
            <p class="text-sm opacity-80">Gestión de costes editoriales</p>
        </div>

        <div class="p-6 grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="space-y-4">
                <h2 class="text-lg font-semibold border-b pb-2 text-gray-700">Datos del Proyecto</h2>
                
                <div>
                    <label class="block text-sm font-medium text-gray-600">Tirada (Unidades)</label>
                    <input type="number" id="tirada" value="15000" class="w-full p-2 border rounded-md bg-yellow-50 focus:ring-2 focus:ring-blue-500 outline-none">
                </div>

                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-medium text-gray-600">Páginas Interior</label>
                        <input type="number" id="pag_int" value="192" class="w-full p-2 border rounded-md bg-yellow-50">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-600">Páginas Cubierta</label>
                        <input type="number" id="pag_cub" value="4" class="w-full p-2 border rounded-md bg-yellow-50">
                    </div>
                </div>

                <h2 class="text-lg font-semibold border-b pb-2 pt-4 text-gray-700">Especificaciones Papel</h2>
                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs font-bold text-gray-500 uppercase">Interior (Gramaje)</label>
                        <input type="number" id="gram_int" value="150" class="w-full p-2 border rounded-md">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-gray-500 uppercase">Cubierta (Gramaje)</label>
                        <input type="number" id="gram_cub" value="350" class="w-full p-2 border rounded-md">
                    </div>
                </div>
            </div>

            <div class="bg-gray-50 p-6 rounded-xl border border-gray-200">
                <h2 class="text-xl font-bold text-gray-800 mb-6">Resumen de Costes</h2>
                
                <div class="space-y-4">
                    <div class="flex justify-between items-center">
                        <span class="text-gray-600">Coste Interior:</span>
                        <span id="res_int" class="font-mono font-bold text-blue-700">0.00 €</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span class="text-gray-600">Coste Cubierta:</span>
                        <span id="res_cub" class="font-mono font-bold text-blue-700">0.00 €</span>
                    </div>
                    <hr class="border-gray-300">
                    <div class="flex justify-between items-center py-2">
                        <span class="text-lg font-bold text-gray-800">TOTAL ESTIMADO:</span>
                        <span id="total_final" class="text-2xl font-black text-green-600">0.00 €</span>
                    </div>
                    <div class="text-center pt-4">
                        <button onclick="calcular()" class="w-full bg-blue-900 hover:bg-blue-800 text-white font-bold py-3 rounded-lg transition">
                            CALCULAR AHORA
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        function calcular() {
            // Valores capturados de la interfaz
            const tirada = parseFloat(document.getElementById('tirada').value);
            const pagInt = parseFloat(document.getElementById('pag_int').value);
            const gramInt = parseFloat(document.getElementById('gram_int').value);
            
            // Constantes extraídas de tu CSV (puedes hacerlas editables luego)
            const anchoInt = 80; const largoInt = 63;
            const precioPapelInt = 1.02;
            const mermaFijaInt = 2350;
            const mermaSucesivaInt = 1.08;

            // Lógica de cálculo (Cerebro de la App)
            const pesoHojaInt = (anchoInt * largoInt * gramInt) / 10000;
            const pliegosNecesarios = (tirada * (pagInt / 16) * mermaSucesivaInt) + mermaFijaInt;
            const totalInt = (pliegosNecesarios * (pesoHojaInt / 1000) * precioPapelInt) + 250; // +250 de fijos

            // Ejemplo simplificado para cubierta
            const totalCub = (tirada * 0.15) + 250; 

            // Mostrar resultados
            document.getElementById('res_int').innerText = totalInt.toLocaleString('de-DE', {minimumFractionDigits: 2}) + " €";
            document.getElementById('res_cub').innerText = totalCub.toLocaleString('de-DE', {minimumFractionDigits: 2}) + " €";
            document.getElementById('total_final').innerText = (totalInt + totalCub).toLocaleString('de-DE', {minimumFractionDigits: 2}) + " €";
        }

        // Ejecutar al cargar
        window.onload = calcular;
    </script>
</body>
</html>
