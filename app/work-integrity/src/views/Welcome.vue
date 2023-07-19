<script setup>
</script>

<template>
    <v-app>
        <v-row align="center" justify="center" class="full-height">
            <v-col cols="12" sm="8" md="6" lg="4">
                <v-card outlined class="welcome-card">
                    <img src="../assets/logo-russas.png" class="logo" />
                    <v-card-text>
                        <h2 class="text-center">Bem-vindo à UFC Russas</h2>
                        <p class="text-center">Efetue o login para continuar!</p>
                    </v-card-text>
                    <RouterLink to="/sign-in">
                        <v-card-actions>
                            <v-btn block>
                                Login
                            </v-btn>
                        </v-card-actions>
                    </RouterLink>
                </v-card>
            </v-col>
        </v-row>
    </v-app>
</template>
  
  
<style scoped lang="scss">
$background: var(--background);
$highlights: var(--highlights);

.full-height {
    background-size: cover;
    background-position: center;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background: url('../assets/campus-ufc-russas.jpg') no-repeat bottom;
    height: 100%;
}

.welcome-card {
    padding: 50px;
    text-align: center;
    max-width: 800px;
    margin: 0 auto;
    background-color: $background;
    border-radius: 8px;
    box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.15);
}

.logo {
    width: 100%;
    margin-bottom: 24px;
}

.text-center {
    text-align: center;
}

.v-btn {
    border-radius: 24px;
    font-weight: bold;
    background-color: $highlights;
    color: $background;
}
</style>